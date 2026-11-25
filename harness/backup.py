"""Backup and restore check. See docs/backup.md.

    crucible backup take [DEST]     write DEST/crucible-<stamp>/ (default ~/crucible-backups)
    crucible backup verify DIR      restore DIR's dump into a scratch database and compare

Everything expensive is small: the database dump, the candidates bucket,
adapters/ and every solution's data/ (sealed held-out included). Langfuse
traces, model weights and images are skipped as re-creatable.

The manifest is what makes it a backup rather than a copy. Row counts are
taken in the same snapshot pg_dump reads (an exported snapshot), so a restore
must match them exactly, even with timer jobs writing events meanwhile.

.env is included only when run from a terminal, encrypted with a passphrase
gpg asks for; unattended, it is skipped and the manifest says so.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from harness import events

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DEST = Path(os.environ.get("CRUCIBLE_BACKUP_DIR", Path.home() / "crucible-backups"))
PG_CONTAINER = "crucible-postgres-1"
DATABASE = "crucible"
SCRATCH = "crucible_restore_check"
TABLES = ("iteration", "elite", "event", "lesson")


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _pg(*args: str, stdin=None) -> subprocess.CompletedProcess:
    """A Postgres client tool inside the database container."""
    return subprocess.run(["docker", "exec", "-i", "-e", f"PGPASSWORD={os.environ['POSTGRES_PASSWORD']}",
                           PG_CONTAINER, *args], stdin=stdin, capture_output=True, check=True)


def _counts(conn) -> dict[str, int]:
    return {t: conn.execute(f"select count(*) from {t}").fetchone()[0] for t in TABLES}


def _git() -> tuple[str, bool]:
    sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=REPO_ROOT,
                                capture_output=True, text=True).stdout.strip())
    return sha, dirty


def _copy_tree(src: Path, dst: Path, files: dict[str, str], root: Path) -> None:
    for p in sorted(src.rglob("*")):
        if p.is_file():
            out = dst / p.relative_to(src)
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)
            files[str(out.relative_to(root))] = _sha256(out)


def take(conn, dest: Path, with_env: bool) -> Path:
    from harness.storage import BUCKET, s3_client

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    final = dest / f"crucible-{stamp}"
    work = dest / f"crucible-{stamp}.partial"
    work.mkdir(parents=True)

    # Counts and dump from one snapshot. The exporting transaction must stay
    # open until pg_dump has attached to it.
    conn.commit()
    with conn.transaction():
        conn.execute("set transaction isolation level repeatable read")
        snapshot = conn.execute("select pg_export_snapshot()").fetchone()[0]
        counts = _counts(conn)
        with (work / "crucible.dump").open("wb") as f:
            subprocess.run(["docker", "exec", "-e", f"PGPASSWORD={os.environ['POSTGRES_PASSWORD']}", PG_CONTAINER,
                            "pg_dump", "-U", "postgres", "-Fc", f"--snapshot={snapshot}", DATABASE],
                           stdout=f, check=True)

    s3 = s3_client()
    n_obj = n_bytes = 0
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET):
        for o in page.get("Contents", []):
            out = work / "candidates" / o["Key"]
            out.parent.mkdir(parents=True, exist_ok=True)
            s3.download_file(BUCKET, o["Key"], str(out))
            n_obj, n_bytes = n_obj + 1, n_bytes + o["Size"]

    files: dict[str, str] = {}
    _copy_tree(REPO_ROOT / "adapters", work / "adapters", files, work)
    for data in sorted((REPO_ROOT / "solutions").glob("*/data")):
        _copy_tree(data, work / "data" / data.parent.name, files, work)

    env = "skipped: no terminal to ask for a passphrase"
    if with_env:
        subprocess.run(["gpg", "--symmetric", "--cipher-algo", "AES256", "--output", str(work / "env.gpg"),
                        str(REPO_ROOT / ".env")], check=True)
        env = "env.gpg, gpg symmetric AES256"

    sha, dirty = _git()
    digest = (REPO_ROOT / ".container-digest").read_text().strip()
    manifest = {
        "taken_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "git_sha": sha, "git_dirty": dirty, "container_digest": digest,
        "rows": counts,
        "dump": {"file": "crucible.dump", "sha256": _sha256(work / "crucible.dump"),
                 "bytes": (work / "crucible.dump").stat().st_size},
        "candidates": {"objects": n_obj, "bytes": n_bytes},
        "env": env,
        "files": files,
    }
    (work / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    work.rename(final)
    events.record(conn, "backup", None, path=str(final), rows=counts, candidates=n_obj,
                  mb=round(sum(p.stat().st_size for p in final.rglob("*") if p.is_file()) / 1e6, 1))
    return final


def compare(manifest: dict, rows: dict[str, int], dump_sha: str, n_candidates: int,
            files: dict[str, str]) -> list[str]:
    """Every difference between a manifest and what a restore found. Empty
    means the restore is verified."""
    bad = [f"{t}: manifest {n}, restored {rows.get(t)}" for t, n in manifest["rows"].items() if rows.get(t) != n]
    if dump_sha != manifest["dump"]["sha256"]:
        bad.append("dump sha256 differs from the manifest")
    if n_candidates != manifest["candidates"]["objects"]:
        bad.append(f"candidates: manifest {manifest['candidates']['objects']}, found {n_candidates}")
    bad += [f"{f}: missing or changed" for f, h in manifest["files"].items() if files.get(f) != h]
    return bad


def verify(conn, root: Path) -> list[str]:
    manifest = json.loads((root / "manifest.json").read_text())
    _pg("dropdb", "-U", "postgres", "--if-exists", SCRATCH)
    _pg("createdb", "-U", "postgres", SCRATCH)
    try:
        with (root / "crucible.dump").open("rb") as f:
            _pg("pg_restore", "-U", "postgres", "--no-owner", "-d", SCRATCH, stdin=f)
        q = " union all ".join(f"select '{t}', count(*) from {t}" for t in TABLES)
        out = _pg("psql", "-U", "postgres", "-d", SCRATCH, "-At", "-c", q).stdout.decode()
        rows = {t: int(n) for t, n in (line.split("|") for line in out.split())}
    finally:
        _pg("dropdb", "-U", "postgres", "--if-exists", SCRATCH)
    files = {f: _sha256(root / f) for f in manifest["files"] if (root / f).exists()}
    n_candidates = sum(1 for p in (root / "candidates").rglob("*") if p.is_file())
    bad = compare(manifest, rows, _sha256(root / "crucible.dump"), n_candidates, files)
    events.record(conn, "restore_check", None, path=str(root), ok=not bad, rows=rows, problems=bad)
    return bad


def main() -> int:
    from harness.persistence import connect

    ap = argparse.ArgumentParser(description="docs/backup.md: take a backup, or verify one by restoring it")
    ap.add_argument("cmd", choices=["take", "verify"])
    ap.add_argument("path", nargs="?", type=Path)
    a = ap.parse_args()
    with connect() as conn:
        if a.cmd == "take":
            out = take(conn, a.path or DEFAULT_DEST, with_env=sys.stdin.isatty())
            m = json.loads((out / "manifest.json").read_text())
            print(f"backup: {out}")
            print(f"rows: {m['rows']}; candidates: {m['candidates']['objects']}; env: {m['env']}")
            return 0
        if not a.path:
            ap.error("verify needs the backup directory")
        bad = verify(conn, a.path)
        print("restore check: " + ("ok, every count and checksum matches the manifest" if not bad else "FAILED"))
        for b in bad:
            print(f"  {b}")
        return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
