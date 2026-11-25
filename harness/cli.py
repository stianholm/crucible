"""Command-line entrypoint. `python -m harness.cli onboard` runs the wizard."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.prompt import Confirm, Prompt
from rich.table import Table

from harness.onboarding import ARCHETYPES, MEASUREMENT_CHOICES, OnboardingAnswers, onboard, slugify

REPO_ROOT = Path(__file__).resolve().parent.parent


def _show_archetype_table(console: Console) -> None:
    t = Table(title="Archetypes — help for questions 2 and 3")
    t.add_column("Archetype")
    t.add_column("Artifact")
    t.add_column("Invocation")
    t.add_column("Fitness usually rests on")
    for v in ARCHETYPES.values():
        t.add_row(v["label"], v["artifact"], v["invocation"], v["fitness_usually_rests_on"])
    console.print(t)


def run_wizard(console: Console) -> tuple[str, OnboardingAnswers]:
    console.print("[bold]Onboarding a solution[/bold] — eight questions, frozen forever on one of them.\n")

    q1 = Prompt.ask("[1/8] What is the thing that should get better? One sentence")

    _show_archetype_table(console)
    q2 = Prompt.ask("[2/8] What form does it take?")

    console.print(
        "\n[bold yellow]Question 3 is frozen forever.[/bold yellow] If this changes later, "
        "every score in this solution's archive becomes incomparable and the solution starts over.\n"
    )
    q3 = Prompt.ask("[3/8] How is it invoked? (function signature, CLI call, HTTP endpoint)")
    if not Confirm.ask(f"Confirm invocation is frozen as: [bold]{q3}[/bold]?", default=True):
        q3 = Prompt.ask("[3/8] How is it invoked?")

    q4 = Prompt.ask("[4/8] What may the proposer change, and what is frozen scaffolding?")
    q5 = Prompt.ask("[5/8] How do you tell a good version from a bad one, even informally?")

    console.print(
        "\n[6/8] What can you measure against?\n"
        "  automated_checks  — [green]preferred[/green]: partial credit for free, deterministic, can't be gamed by argument\n"
        "  labelled_examples — needs a human-labelled set\n"
        "  judge             — needs an LLM rubric; competes with the proposer for GPU bandwidth\n"
        "  none_yet          — decide during Phase 1\n"
    )
    q6 = Prompt.ask("Answer", choices=list(MEASUREMENT_CHOICES), default="automated_checks")
    if q6 in ("labelled_examples", "judge"):
        console.print(
            "[yellow]Automated checks are preferred where possible[/yellow] — they give partial "
            "credit for free, keep the noise floor small, and don't compete with the proposer for "
            "memory bandwidth the way judge calls do. Reconsider if some of this can be checked "
            "programmatically.\n"
        )
        if not Confirm.ask(f"Keep '{q6}' as the answer?", default=True):
            q6 = Prompt.ask("Answer", choices=list(MEASUREMENT_CHOICES))

    q7 = Confirm.ask("[7/8] Does evaluating a candidate require executing code?")

    console.print(
        "\n[8/8] Is there a written standard the solution must follow (a spec, a policy, the rules a "
        "reviewer applies)? If so, state it. The proposer is given it from the first generation, so "
        "search spends its effort on what [bold]can't[/bold] be written down. Leave blank if there is none.\n"
    )
    q8 = Prompt.ask("Standard", default="")

    answers = OnboardingAnswers(
        q1_what=q1,
        q2_form=q2,
        q3_invocation=q3,
        q4_mutation_surface=q4,
        q5_good_vs_bad=q5,
        q6_measurement=q6,
        q7_executes_code=q7,
        q8_standard=q8,
    )
    solution_id = slugify(Prompt.ask("Solution id (short, kebab-case)", default=slugify(q1)))
    return solution_id, answers


def cmd_onboard(_args: argparse.Namespace) -> int:
    console = Console()
    solution_id, answers = run_wizard(console)
    sol_dir = onboard(solution_id, answers, REPO_ROOT)
    console.print(f"\n[bold green]Created {sol_dir.relative_to(REPO_ROOT)}/[/bold green]")
    console.print("Next: populate candidate/, checks/, data/, and BASELINE.yaml.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="harness")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("onboard", help="Run the onboarding wizard").set_defaults(func=cmd_onboard)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
