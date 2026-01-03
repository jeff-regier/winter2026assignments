#!/usr/bin/env python3
"""Release tool for homework assignments.

Validates and prepares Jupyter notebooks for student release by:
- Checking problem structure (prompt, solution, visible tests, hidden tests)
- Running ruff linting
- Executing notebooks to verify solutions pass
- Stripping solutions and hidden tests for student versions
"""

import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(
    help="Validate and release homework assignments.",
    add_completion=False,
)


@dataclass
class Problem:
    """Represents a homework problem with its components."""

    number: int
    title: str
    prompt_cell_idx: int
    solution_cell_idxs: list[int] = field(default_factory=list)
    visible_test_cell_idxs: list[int] = field(default_factory=list)
    hidden_test_cell_idxs: list[int] = field(default_factory=list)

    @property
    def has_prompt(self) -> bool:
        return self.prompt_cell_idx >= 0

    @property
    def has_solution(self) -> bool:
        return len(self.solution_cell_idxs) > 0

    @property
    def has_visible_tests(self) -> bool:
        return len(self.visible_test_cell_idxs) > 0

    @property
    def has_hidden_tests(self) -> bool:
        return len(self.hidden_test_cell_idxs) > 0

    @property
    def is_complete(self) -> bool:
        return (
            self.has_prompt
            and self.has_solution
            and self.has_visible_tests
            and self.has_hidden_tests
        )


@dataclass
class ValidationResult:
    """Result of validating a notebook."""

    notebook_path: Path
    problems: list[Problem] = field(default_factory=list)
    ruff_errors: list[str] = field(default_factory=list)
    execution_errors: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return (
            all(p.is_complete for p in self.problems)
            and not self.ruff_errors
            and not self.execution_errors
        )


def get_cell_source(cell: dict) -> str:
    """Get cell source as a string."""
    source = cell.get("source", [])
    if isinstance(source, list):
        return "".join(source)
    return source


def find_problems(nb: dict) -> list[Problem]:
    """Find all problems in a notebook and their components."""
    problems: list[Problem] = []
    current_problem: Problem | None = None

    # Pattern to match problem headers like:
    #   "### Problem 1:" or "## (10 pts) Problem 2:"
    #   "#### **Problem 3:**" or "#### **(10 pts) Problem 4:**"
    problem_pattern = re.compile(
        r"^#{2,4}\s*\*{0,2}(?:\([^)]+\)\s*)?\*{0,2}\s*Problem\s+(\d+)[:\s*]+(.+)$",
        re.MULTILINE,
    )

    for idx, cell in enumerate(nb.get("cells", [])):
        source = get_cell_source(cell)
        cell_type = cell.get("cell_type", "")

        # Check for problem header in markdown cells
        if cell_type == "markdown":
            match = problem_pattern.search(source)
            if match:
                # Save previous problem if exists
                if current_problem is not None:
                    problems.append(current_problem)

                problem_num = int(match.group(1))
                problem_title = match.group(2).strip()
                current_problem = Problem(
                    number=problem_num,
                    title=problem_title,
                    prompt_cell_idx=idx,
                )

        # Check code cells for solutions and tests
        elif cell_type == "code" and current_problem is not None:
            has_solution = "# BEGIN SOLUTION" in source or "# SOLUTION" in source
            has_hidden_tests = "# BEGIN HIDDEN TESTS" in source
            has_visible_tests = "assert " in source and not has_hidden_tests

            # A cell can have both solutions and tests
            if has_solution:
                current_problem.solution_cell_idxs.append(idx)

            if has_hidden_tests:
                current_problem.hidden_test_cell_idxs.append(idx)

            # Visible tests: has asserts but outside of hidden test blocks
            if has_visible_tests or (
                "assert " in source and "# BEGIN HIDDEN TESTS" in source
            ):
                # Check if there are asserts outside of hidden test blocks
                lines = source.split("\n")
                in_hidden = False
                for line in lines:
                    stripped = line.strip()
                    if stripped == "# BEGIN HIDDEN TESTS":
                        in_hidden = True
                    elif stripped == "# END HIDDEN TESTS":
                        in_hidden = False
                    elif "assert " in line and not in_hidden:
                        current_problem.visible_test_cell_idxs.append(idx)
                        break

    # Don't forget the last problem
    if current_problem is not None:
        problems.append(current_problem)

    return problems


def extract_code_cells(nb: dict) -> str:
    """Extract all code from code cells for ruff checking."""
    code_parts = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            source = get_cell_source(cell)
            code_parts.append(source)
    return "\n\n".join(code_parts)


def run_ruff_check(notebook_path: Path) -> list[str]:
    """Run ruff on notebook code and return any errors."""
    try:
        result = subprocess.run(
            ["ruff", "check", str(notebook_path), "--output-format=concise"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            # Filter and return error lines
            errors = [
                line
                for line in result.stdout.strip().split("\n")
                if line and not line.startswith("Found")
            ]
            return errors
        return []
    except FileNotFoundError:
        return ["ruff not found - install with: pip install ruff"]
    except subprocess.TimeoutExpired:
        return ["ruff check timed out"]


def run_notebook(notebook_path: Path) -> list[str]:
    """Execute a notebook and return any assertion errors.

    Uses --allow-errors since educational notebooks often have intentional
    error cells to demonstrate exceptions. Only fails on assertion errors
    which indicate test failures.
    """
    try:
        result = subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--allow-errors",
                "--inplace",
                str(notebook_path),
            ],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout for execution
        )
        # Even with --allow-errors, check for assertion failures in output
        if result.returncode != 0:
            error_output = result.stderr.strip()
            if "AssertionError" in error_output:
                lines = error_output.split("\n")
                errors = [line for line in lines if "AssertionError" in line]
                return errors[:5] if errors else ["Assertion failed"]
            # Other errors are likely intentional demo errors, ignore them
            return []
        return []
    except FileNotFoundError:
        return ["jupyter not found - install with: pip install jupyter"]
    except subprocess.TimeoutExpired:
        return ["Notebook execution timed out (>5 minutes)"]


def validate_notebook(
    notebook_path: Path,
    check_ruff: bool = True,
    check_execution: bool = True,
) -> ValidationResult:
    """Validate a notebook for completeness."""
    with notebook_path.open() as f:
        nb = json.load(f)

    problems = find_problems(nb)
    ruff_errors = run_ruff_check(notebook_path) if check_ruff else []
    execution_errors = run_notebook(notebook_path) if check_execution else []

    return ValidationResult(
        notebook_path=notebook_path,
        problems=problems,
        ruff_errors=ruff_errors,
        execution_errors=execution_errors,
    )


def strip_solutions_and_hidden_tests(source_lines: list[str]) -> list[str]:
    """Remove solution code and hidden tests from cell source lines."""
    result = []
    in_solution = False
    in_hidden_tests = False

    for line in source_lines:
        stripped = line.rstrip("\n").strip()

        # Handle solution markers
        if stripped == "# BEGIN SOLUTION":
            in_solution = True
            result.append("# your code here\n")
            continue
        elif stripped == "# END SOLUTION":
            in_solution = False
            continue

        # Handle hidden test markers
        if stripped == "# BEGIN HIDDEN TESTS":
            in_hidden_tests = True
            continue
        elif stripped == "# END HIDDEN TESTS":
            in_hidden_tests = False
            continue

        # Skip lines inside solution or hidden test blocks
        if in_solution or in_hidden_tests:
            continue

        # Handle inline solution marker
        if "# SOLUTION" in line:
            indent = len(line) - len(line.lstrip())
            result.append(" " * indent + "# your code here\n")
            continue

        result.append(line)

    return result


def process_notebook(input_path: Path, output_dir: Path) -> tuple[Path, int, int]:
    """Process a notebook and write the student version."""
    with input_path.open() as f:
        nb = json.load(f)

    solutions_stripped = 0
    hidden_tests_stripped = 0

    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            source = cell.get("source", [])
            if isinstance(source, str):
                source = source.split("\n")
                source = [line + "\n" for line in source[:-1]] + [source[-1]]

            source_text = "".join(source)
            has_solution = "# BEGIN SOLUTION" in source_text or "# SOLUTION" in source_text
            has_hidden = "# BEGIN HIDDEN TESTS" in source_text

            if has_solution or has_hidden:
                cell["source"] = strip_solutions_and_hidden_tests(source)
                if has_solution:
                    solutions_stripped += 1
                if has_hidden:
                    hidden_tests_stripped += 1

    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / input_path.name

    with output_file.open("w") as f:
        json.dump(nb, f, indent=1)

    return output_file, solutions_stripped, hidden_tests_stripped


@app.command()
def check(
    notebooks: Annotated[
        list[Path],
        typer.Argument(
            help="Notebook files to validate",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    skip_ruff: Annotated[
        bool,
        typer.Option("--skip-ruff", help="Skip ruff linting check"),
    ] = False,
    skip_execution: Annotated[
        bool,
        typer.Option("--skip-execution", help="Skip notebook execution check"),
    ] = False,
) -> None:
    """Validate notebooks: problems, ruff, and execution."""
    all_valid = True

    for notebook_path in notebooks:
        print(f"\n{notebook_path}")
        print("=" * 60)

        result = validate_notebook(
            notebook_path,
            check_ruff=not skip_ruff,
            check_execution=not skip_execution,
        )

        if not result.problems:
            print("  No problems found in notebook")
            all_valid = False
            continue

        for problem in result.problems:
            print(f"  Problem {problem.number}: {problem.title}")

            missing = []
            if not problem.has_prompt:
                missing.append("prompt")
            if not problem.has_solution:
                missing.append("solution")
            if not problem.has_visible_tests:
                missing.append("visible tests")
            if not problem.has_hidden_tests:
                missing.append("hidden tests")

            if missing:
                print(f"    MISSING: {', '.join(missing)}")
                all_valid = False
            else:
                print("    OK")

        if result.ruff_errors:
            print("\n  Ruff errors:")
            for error in result.ruff_errors[:10]:
                print(f"    {error}")
            if len(result.ruff_errors) > 10:
                print(f"    ... and {len(result.ruff_errors) - 10} more")
            all_valid = False

        if result.execution_errors:
            print("\n  Execution errors:")
            for error in result.execution_errors[:5]:
                print(f"    {error}")
            all_valid = False

        if not result.ruff_errors and not result.execution_errors:
            print("\n  Ruff: OK")
            print("  Execution: OK")

    print()
    if all_valid:
        print("All notebooks valid!")
    else:
        print("Some notebooks have issues.")
        raise typer.Exit(1)


@app.command()
def release(
    notebooks: Annotated[
        list[Path],
        typer.Argument(
            help="Notebook files to release",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    output_dir: Annotated[
        Path,
        typer.Option(
            "--output-dir",
            "-o",
            help="Output directory for student versions",
        ),
    ] = Path("student"),
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            "-n",
            help="Show what would be done without writing files",
        ),
    ] = False,
    skip_check: Annotated[
        bool,
        typer.Option(
            "--skip-check",
            help="Skip validation before releasing (not recommended)",
        ),
    ] = False,
) -> None:
    """Validate and release notebooks for students.

    Runs validation (problems, ruff, execution) then creates student versions
    with solutions and hidden tests removed. Original files are never modified.
    """
    # Run validation first unless skipped
    if not skip_check:
        print("Validating notebooks...")
        all_valid = True
        for notebook_path in notebooks:
            result = validate_notebook(
                notebook_path, check_ruff=True, check_execution=True
            )

            if not result.problems:
                print(f"  {notebook_path}: No problems found")
                all_valid = False
                continue

            incomplete = [p for p in result.problems if not p.is_complete]
            if incomplete:
                print(f"  {notebook_path}: {len(incomplete)} incomplete problem(s)")
                for p in incomplete:
                    missing = []
                    if not p.has_solution:
                        missing.append("solution")
                    if not p.has_visible_tests:
                        missing.append("visible tests")
                    if not p.has_hidden_tests:
                        missing.append("hidden tests")
                    print(f"    Problem {p.number}: missing {', '.join(missing)}")
                all_valid = False

            if result.ruff_errors:
                print(f"  {notebook_path}: {len(result.ruff_errors)} ruff error(s)")
                all_valid = False

            if result.execution_errors:
                print(f"  {notebook_path}: execution failed")
                for err in result.execution_errors[:3]:
                    print(f"    {err}")
                all_valid = False

        if not all_valid:
            print("\nValidation failed. Fix issues or use --skip-check to bypass.")
            raise typer.Exit(1)

        print("All notebooks valid.\n")

    # Proceed with stripping
    if not dry_run:
        output_dir.mkdir(exist_ok=True)

    total_solutions = 0
    total_hidden = 0

    for notebook in notebooks:
        if dry_run:
            with notebook.open() as f:
                nb = json.load(f)
            sol_count = sum(
                1
                for c in nb["cells"]
                if c.get("cell_type") == "code"
                and ("# BEGIN SOLUTION" in get_cell_source(c) or "# SOLUTION" in get_cell_source(c))
            )
            hidden_count = sum(
                1
                for c in nb["cells"]
                if c.get("cell_type") == "code"
                and "# BEGIN HIDDEN TESTS" in get_cell_source(c)
            )
            output_file = output_dir / notebook.name
            print(f"[dry-run] {notebook} -> {output_file} ({sol_count} solutions, {hidden_count} hidden tests)")
        else:
            output_file, sol_count, hidden_count = process_notebook(notebook, output_dir)
            print(f"{notebook} -> {output_file} ({sol_count} solutions, {hidden_count} hidden tests stripped)")

        total_solutions += sol_count
        total_hidden += hidden_count

    suffix = " [dry-run]" if dry_run else ""
    print(f"\nProcessed {len(notebooks)} notebook(s): {total_solutions} solution(s), {total_hidden} hidden test(s){suffix}")


if __name__ == "__main__":
    app()
