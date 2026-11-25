"""The onboarding wizard's eighth question: a written standard for the proposer."""

import yaml

from harness.onboarding import OnboardingAnswers, onboard, task_description


def _answers(**kw):
    base = dict(q1_what="Route tickets.", q2_form="prompt", q3_invocation="invoke()", q4_mutation_surface="block",
                q5_good_vs_bad="correct routes", q6_measurement="automated_checks", q7_executes_code=False)
    return OnboardingAnswers(**(base | kw))


def test_standard_reaches_the_task_description(tmp_path):
    sol = onboard("t1", _answers(q8_standard="Refunds over 500 go to finance."), tmp_path)
    assert yaml.safe_load((sol / "solution.yaml").read_text())["standard"] == "Refunds over 500 go to finance."
    assert task_description(sol) == "Route tickets.\n\nThe standard it must meet: Refunds over 500 go to finance."
    assert "Refunds over 500" in (sol / "SOLUTION.md").read_text()


def test_no_standard_leaves_the_description_as_question_one(tmp_path):
    sol = onboard("t2", _answers(), tmp_path)
    assert task_description(sol) == "Route tickets."
    assert "None stated" in (sol / "SOLUTION.md").read_text()


def test_existing_solution_yaml_without_the_field_still_works(tmp_path):
    sol = tmp_path / "old"; sol.mkdir()
    (sol / "solution.yaml").write_text(yaml.safe_dump({"what": "Classify gateways."}))
    assert task_description(sol) == "Classify gateways."
