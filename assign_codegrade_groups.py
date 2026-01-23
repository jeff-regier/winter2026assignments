#!/usr/bin/env python3
"""Create random student groups for a CodeGrade course."""

import os
import random
from enum import StrEnum
from typing import Annotated

import codegrade
import codegrade.models as cg_models
import typer
from rich.console import Console

console = Console()

CODEGRADE_TENANT = "0be7f466-9745-4aed-bfc7-7d77576f5e7b"


class Course(StrEnum):
    datasci315 = "datasci315"
    datasci503 = "datasci503"


COURSE_IDS = {"datasci315": 17676, "datasci503": 17677}


def get_client():
    """Get authenticated CodeGrade client."""
    if (user := os.environ.get("CODEGRADE_USERNAME")) and (
        pw := os.environ.get("CODEGRADE_PASSWORD")
    ):
        return codegrade.login(username=user, password=pw, tenant=CODEGRADE_TENANT)
    return codegrade.login_from_cli()


def get_students(client, course_id: int) -> list[dict]:
    """Get all students in a course (excluding test students)."""
    students = []
    for enrollment in client.course.get_all_users(course_id=course_id, page_size=100):
        if "student" in enrollment.course_role.name.lower():
            user = enrollment.raw_data.get("user", {}) if enrollment.raw_data else {}
            name = user.get("name", "Unknown")
            if name != "Test Student":
                students.append({"id": user.get("id"), "name": name})
    return students


def partition_students(students: list[dict]) -> list[list[dict]]:
    """Partition students into groups of 2. Last group gets 3 if there'd be a singleton."""
    random.shuffle(students)
    n = len(students)

    if n % 2 == 1 and n > 2:
        return [students[i : i + 2] for i in range(0, n - 3, 2)] + [students[n - 3 :]]

    return [students[i : i + 2] for i in range(0, n, 2)]


def create_groups(client, group_set_id: int | None, groups: list[list[dict]], *, dry_run: bool):
    """Create groups in CodeGrade."""
    for i, members in enumerate(groups, 1):
        names = ", ".join(m["name"] for m in members)
        console.print(f"  [cyan]Group {i}[/cyan]: {names}")

        if not dry_run:
            try:
                client.group_set.create_group(
                    group_set_id=group_set_id,
                    json_body=cg_models.CreateGroupGroupSetData(
                        member_ids=[m["id"] for m in members],
                    ),
                )
            except Exception as e:
                console.print(f"    [red]ERROR: {e}[/red]")


def main(
    course: Annotated[Course, typer.Argument(help="Course to create groups for")],
    dry_run: Annotated[bool, typer.Option("--dry-run", "-n", help="Preview only")] = False,
):
    """Create random student groups of 2 for a course."""
    client = get_client()
    course_id = COURSE_IDS[course]

    course_info = client.course.get(course_id=course_id)
    console.print(f"\n[bold]Course:[/bold] {course_info.name}")

    students = get_students(client, course_id)
    console.print(f"[bold]Students:[/bold] {len(students)}")

    if not students:
        console.print("[yellow]No students found![/yellow]")
        raise typer.Exit(0)

    groups = partition_students(students)

    console.print(f"\n[bold]Creating {len(groups)} groups[/bold]")
    if len(groups[-1]) != 2:
        console.print(f"[dim](last group has {len(groups[-1])} students)[/dim]")

    group_set_id = None
    if not dry_run:
        group_set = client.course.create_group_set(
            course_id=course_id,
            json_body=cg_models.CreateGroupSetCourseData(minimum_size=2, maximum_size=3),
        )
        group_set_id = group_set.id
        console.print(f"Created group set (ID: {group_set_id})\n")

    create_groups(client, group_set_id, groups, dry_run=dry_run)

    if dry_run:
        console.print("\n[yellow][DRY RUN] No changes made.[/yellow]")
    else:
        console.print(f"\n[green]Done! Group Set ID: {group_set_id}[/green]")


if __name__ == "__main__":
    typer.run(main)
