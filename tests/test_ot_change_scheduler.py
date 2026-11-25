"""ot_change_scheduler: the rules, the exact optimum, and the score."""

import json

from harness.types import Task
from solutions.ot_change_scheduler.adapter import OtChangeSchedulerAdapter
from solutions.ot_change_scheduler.checks.generate_tasks import generate, optimum
from solutions.ot_change_scheduler.checks.model import verify


def tiny():
    return {"instance_id": "t", "zones": ["Z1", "Z2"], "conflicts": [["Z1", "Z2"]],
            "windows": [{"id": "W1", "order": 1, "crew_hours": 10, "max_outages": 1},
                        {"id": "W2", "order": 2, "crew_hours": 10, "max_outages": 1}],
            "changes": [
                {"id": "A", "zone": "Z1", "hours": 6, "value": 5, "outage": True, "depends_on": [], "deadline": None},
                {"id": "B", "zone": "Z2", "hours": 6, "value": 4, "outage": True, "depends_on": ["A"], "deadline": None},
                {"id": "C", "zone": "Z2", "hours": 4, "value": 3, "outage": False, "depends_on": [], "deadline": "W1"},
            ]}


def test_each_rule_is_enforced():
    inst = tiny()
    assert verify(inst, {"A": "W1", "B": "W2", "C": "W1"}) == ([], 12)
    assert verify(inst, {"A": "W1", "C": "W2"})[0]                    # deadline
    assert verify(inst, {"B": "W2"})[0]                               # dependency missing
    assert verify(inst, {"A": "W2", "B": "W2"})[0]                    # not strictly earlier
    two = tiny(); two["windows"][0]["max_outages"] = 2
    two["changes"][1]["depends_on"] = []
    assert any("conflicting" in v for v in verify(two, {"A": "W1", "B": "W1"})[0])
    assert any("capacity" in v for v in verify(two, {"A": "W1", "B": "W1"})[0])
    assert verify(inst, {"A": "W9"})[0] and verify(inst, {"Z": "W1"})[0] and verify(inst, [])[0]


def test_milp_finds_the_optimum_and_verify_agrees():
    value, plan, proven = optimum(tiny())
    assert proven and value == 12 and verify(tiny(), plan) == ([], 12)


def test_instances_rebuild_identically():
    assert generate("otcs-0042") == generate("otcs-0042")
    assert generate("otcs-0042") != generate("otcs-0043")


def test_score_is_value_over_optimum_and_zero_when_invalid():
    a = OtChangeSchedulerAdapter()
    task = Task(task_id="t", input=json.dumps(tiny()), expected={"optimum": 12, "proven": True})
    out = lambda plan: json.dumps({"plan": plan, "n_changes": 3})
    assert a.programmatic_checks(out({"A": "W1", "B": "W2", "C": "W1"}), task)["value"][0] == 1.0
    assert a.programmatic_checks(out({"A": "W1"}), task)["value"][0] == 5 / 12
    assert a.programmatic_checks(out({"B": "W1"}), task) == {"valid_plan": (0.0, "B depends on A, which is not scheduled")}
    assert "parses" in a.programmatic_checks("not json", task)
