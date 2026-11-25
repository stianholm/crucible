"""Replay recorded judge requests and compare outputs (TODO.md decision 71).

Measures whether the judge returns the same verdict for the same input, at the
temperature and concurrency real scoring uses. Run `replay` twice within one
judge lifetime for the noise floor, and again after a restart for the
restart effect.

usage: judge_replay.py fetch OUT.json [judge|proposer] | replay IN.json OUT.json [judge|proposer]
       | compare A.json B.json ...

`proposer` fetches the worker's temperature-0 calls, not the proposal calls
(temperature 0.9), so both halves of capability_case's fitness can be tested.
For a worker call the decision compared is its JSON verdict instead of BAND."""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI

BAND = re.compile(r"BAND\s*:\s*(\d)")


VERDICT = re.compile(r'"verdict"\s*:\s*"([\w-]+)"')


def band(text):
    """The decision in a reply: the judge's last BAND line, else the worker's
    JSON verdict."""
    m = BAND.findall(text or "") or VERDICT.findall(text or "")
    return m[-1] if m else None


def fetch(out, model="judge"):
    q = ("select id, input, output from observations where type='GENERATION' "
         f"and provided_model_name='hosted_vllm/{model}' and JSONExtractString(model_parameters, 'temperature') = '0.0' "
         "and start_time between '2026-10-13 04:10:00' and '2026-10-13 07:00:00' "
         "order by id limit 64 format JSONEachRow")
    raw = subprocess.run(["docker", "exec", "crucible-clickhouse-1", "clickhouse-client",
                          "--password", os.environ["CLICKHOUSE_PASSWORD"], "-q", q],
                         capture_output=True, text=True, check=True).stdout
    rows = []
    for l in raw.splitlines():
        o = json.loads(l)
        try:
            content = json.loads(o["output"])["content"]
        except Exception:
            continue
        rows.append({"id": o["id"], "messages": json.loads(o["input"])["messages"], "original": content})
    json.dump(rows, open(out, "w"))
    print(len(rows), "requests")


def replay(inp, out, model="judge"):
    rows = json.load(open(inp))
    c = OpenAI(base_url="http://localhost:4000", api_key=os.environ.get("LITELLM_API_KEY", "unused"), timeout=1200, max_retries=0)

    def one(r):
        resp = c.chat.completions.create(model=model, temperature=0.0, messages=r["messages"])
        return resp.choices[0].message.content
    with ThreadPoolExecutor(32) as ex:
        outs = list(ex.map(one, rows))
    json.dump(outs, open(out, "w"))
    print("replayed", len(outs))


def compare(paths):
    sets = [json.load(open(p)) for p in paths]
    base = sets[0]
    for p, s in zip(paths[1:], sets[1:]):
        text = sum(a == b for a, b in zip(base, s))
        bands = sum(band(a) == band(b) for a, b in zip(base, s))
        print(f"{paths[0]} vs {p}: identical text {text}/{len(s)}, same decision {bands}/{len(s)}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "fetch":
        fetch(sys.argv[2], *sys.argv[3:4])
    elif cmd == "replay":
        replay(sys.argv[2], sys.argv[3], *sys.argv[4:5])
    elif cmd == "compare":
        compare(sys.argv[2:])
    elif cmd == "original":
        rows = json.load(open(sys.argv[2])); json.dump([r["original"] for r in rows], open(sys.argv[3], "w"))
