"""Drop the page cache held by model weights, without root.

On the GB10's unified memory, CUDA counts only free pages as available, while
the kernel's MemAvailable also counts page cache it could reclaim. Found
2026-10-16: after the proposer stopped and a 62 GB checkpoint download, the
kernel reported 93 GB available and CUDA reported 53.6 GB free, and
gpt-oss-120b's training load failed for want of the difference. Reading
weights fills the cache the same way, so every nightly window starts with
tens of GB that CUDA cannot use.

`echo 3 > /proc/sys/vm/drop_caches` fixes it but needs root.
posix_fadvise(DONTNEED) needs only read access to the file, and evicts just
the files named, which here is everything under the Hugging Face cache.

Usage: python ops/evict_cache.py [dir ...]   default ~/.cache/huggingface
Prints MemFree before and after, in GB.
"""

import os
import sys
from pathlib import Path


def mem_free_gb() -> float:
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemFree:"):
            return int(line.split()[1]) / 2**20
    raise RuntimeError("no MemFree in /proc/meminfo")


def evict(root: Path) -> tuple[int, int]:
    files = size = 0
    for dirpath, _dirs, names in os.walk(root):
        for name in names:
            p = os.path.join(dirpath, name)
            if os.path.islink(p) or not os.path.isfile(p):
                continue  # snapshot entries are symlinks into blobs/, evicted there
            try:
                fd = os.open(p, os.O_RDONLY)
            except PermissionError:
                continue
            try:
                os.posix_fadvise(fd, 0, 0, os.POSIX_FADV_DONTNEED)
                files += 1
                size += os.fstat(fd).st_size
            finally:
                os.close(fd)
    return files, size


if __name__ == "__main__":
    roots = [Path(a) for a in sys.argv[1:]] or [Path.home() / ".cache" / "huggingface"]
    before = mem_free_gb()
    files = size = 0
    for r in roots:
        f, s = evict(r)
        files, size = files + f, size + s
    print(f"evicted {files} files ({size / 2**30:.0f} GB on disk); MemFree {before:.1f} -> {mem_free_gb():.1f} GB")
