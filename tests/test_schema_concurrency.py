"""ensure_schema() under concurrency, as the timer jobs call it (decision 98).

Two nights running, a timer job that had read `iteration` and then recorded
an event deadlocked with another job's schema setup. Needs the live Postgres.
"""

import os
import threading

import pytest

from harness.persistence import connect, ensure_schema

pytestmark = pytest.mark.skipif(not os.environ.get("POSTGRES_PASSWORD"), reason="needs the live Postgres")


def test_concurrent_schema_setup_after_a_read_does_not_deadlock():
    errors = []

    def caller(read_first: bool):
        try:
            with connect() as c:
                if read_first:  # like retention and the morning report
                    c.execute("select count(*) from iteration").fetchone()
                ensure_schema(c)
        except Exception as e:  # noqa: BLE001 - the test is about any failure
            errors.append(type(e).__name__)

    for _ in range(3):
        threads = [threading.Thread(target=caller, args=(i % 2 == 0,)) for i in range(8)]
        [t.start() for t in threads]
        [t.join() for t in threads]
    assert errors == []
