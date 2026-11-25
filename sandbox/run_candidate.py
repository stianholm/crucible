"""Runs inside the sandbox container. Imports the mounted, read-only
candidate and calls its frozen entrypoint. Never trust anything this
process prints as more than "the candidate's output" — it is untrusted
code, run with --network none, --read-only, capped memory/pids, all
capabilities dropped, and as a non-root, nologin user.
"""

import json
import sys

sys.path.insert(0, "/candidate")


def main() -> int:
    task_input = sys.argv[1]
    from candidate import solve  # the only thing this process ever imports from /candidate

    result = solve(task_input)
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
