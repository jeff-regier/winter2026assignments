#!/usr/bin/env python3
"""Release tool for homework assignments.

Validates and prepares Jupyter notebooks for student release by:
- Checking problem structure (prompt, solution, visible tests, hidden tests)
- Running ruff linting
- Executing notebooks to verify solutions pass
- Stripping solutions and hidden tests for student versions

Usage: python make_student_version.py <notebook.ipynb>
"""

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Problem:
    """Represents a homework problem with its components.

    Expected structure (otter-grader style):
    1. Prompt cell (markdown) - contains problem description
    2. Solution cell (code) - contains solution code, NO tests
    3. Test cell (code) - contains visible and hidden tests, NO solution markers

    For free-response problems (markdown solutions):
    1. Prompt cell (markdown) - contains problem description
    2. Solution cell (markdown) - contains solution text with markers
    """

    number: str  # e.g., "1", "2a", "3b"
    title: str
    prompt_cell_idx: int
    solution_cell_idx: int = -1
    test_cell_idx: int = -1
    is_free_response: bool = False  # True if solution is markdown (no tests needed)
    # Track validation errors for this problem
    errors: list[str] = field(default_factory=list)

    @property
    def has_prompt(self) -> bool:
        return self.prompt_cell_idx >= 0

    @property
    def has_solution(self) -> bool:
        return self.solution_cell_idx >= 0

    @property
    def has_tests(self) -> bool:
        return self.test_cell_idx >= 0

    @property
    def is_complete(self) -> bool:
        if self.is_free_response:
            # Free-response problems only need prompt and solution (no tests)
            return self.has_prompt and self.has_solution and not self.errors
        return self.has_prompt and self.has_solution and self.has_tests and not self.errors


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


def has_solution_marker(source: str) -> bool:
    """Check if source contains solution markers."""
    return "# BEGIN SOLUTION" in source or "# SOLUTION" in source


def has_hidden_tests(source: str) -> bool:
    """Check if source contains hidden test markers."""
    return "# BEGIN HIDDEN TESTS" in source


def has_visible_assert(source: str) -> bool:
    """Check if source has assert statements outside hidden test blocks."""
    if "assert " not in source:
        return False
    in_hidden = False
    for line in source.split("\n"):
        stripped = line.strip()
        if stripped == "# BEGIN HIDDEN TESTS":
            in_hidden = True
        elif stripped == "# END HIDDEN TESTS":
            in_hidden = False
        elif "assert " in line and not in_hidden:
            return True
    return False


def has_any_assert(source: str) -> bool:
    """Check if source has any assert statements (visible or hidden)."""
    return "assert " in source


# Pattern to match problem headers like:
#   "### Problem 1:" or "## (10 pts) Problem 2:"
#   "#### **Problem 3:**" or "#### **(10 pts) Problem 4:**"
#   "### Problem 2a:" or "### Problem 3b:" (with letter suffix)
PROBLEM_PATTERN = re.compile(
    r"^#{2,4}\s*\*{0,2}(?:\([^)]+\)\s*)?\*{0,2}\s*Problem\s+(\d+[a-z]?)[:\s*]+(.+)$",
    re.MULTILINE,
)


def find_problems(nb: dict) -> list[Problem]:
    """Find all problems in a notebook and validate their structure.

    Expected structure for each problem:
    1. Prompt cell (markdown) - contains "Problem N: title"
    2. Solution cell (code) - contains solution markers, NO asserts
    3. Test cell (code) - contains asserts (visible + hidden), NO solution markers

    For free-response problems:
    1. Prompt cell (markdown) - contains "Problem N: title"
    2. Solution cell (markdown) - contains solution markers (no tests needed)
    """
    problems: list[Problem] = []
    cells = nb.get("cells", [])

    # First pass: find all problem prompt cells
    prompt_indices: list[tuple[int, int, str]] = []  # (cell_idx, problem_num, title)
    for idx, cell in enumerate(cells):
        if cell.get("cell_type") == "markdown":
            source = get_cell_source(cell)
            match = PROBLEM_PATTERN.search(source)
            if match:
                prompt_indices.append((idx, match.group(1), match.group(2).strip()))

    # Second pass: validate structure for each problem
    for i, (prompt_idx, problem_num, title) in enumerate(prompt_indices):
        problem = Problem(
            number=problem_num,
            title=title,
            prompt_cell_idx=prompt_idx,
        )

        # Determine the range of cells for this problem
        next_prompt_idx = prompt_indices[i + 1][0] if i + 1 < len(prompt_indices) else len(cells)

        # Look for solution cell and test cell in the cells after the prompt
        solution_found = False
        test_found = False

        for idx in range(prompt_idx + 1, next_prompt_idx):
            cell = cells[idx]
            source = get_cell_source(cell)

            # Check for markdown solution cell (free-response problem)
            if cell.get("cell_type") == "markdown" and has_solution_marker(source):
                problem.solution_cell_idx = idx
                problem.is_free_response = True
                solution_found = True
                continue

            if cell.get("cell_type") != "code":
                continue

            cell_has_solution = has_solution_marker(source)
            cell_has_assert = has_any_assert(source)
            cell_has_hidden = has_hidden_tests(source)

            if cell_has_solution and not solution_found:
                # This is the solution cell
                problem.solution_cell_idx = idx
                solution_found = True

                # Validate: solution cell should NOT have asserts
                if cell_has_assert:
                    problem.errors.append(
                        f"Solution cell (cell {idx}) contains assert statements - "
                        "tests should be in a separate cell"
                    )

            elif cell_has_assert and solution_found and not test_found:
                # This is the test cell
                problem.test_cell_idx = idx
                test_found = True

                # Validate: test cell should NOT have solution markers
                if cell_has_solution:
                    problem.errors.append(
                        f"Test cell (cell {idx}) contains solution markers - "
                        "solution should be in the previous cell"
                    )

                # Validate: test cell should have both visible and hidden tests
                if not has_visible_assert(source):
                    problem.errors.append(f"Test cell (cell {idx}) missing visible tests")
                if not cell_has_hidden:
                    problem.errors.append(f"Test cell (cell {idx}) missing hidden tests")

                # Validate: test cell should start with "# Test assertions"
                first_line = source.split("\n")[0].strip() if source else ""
                if first_line != "# Test assertions":
                    problem.errors.append(
                        f"Test cell (cell {idx}) must start with '# Test assertions'"
                    )

        problems.append(problem)

    return problems


def run_ruff_check(notebook_path: Path) -> list[str]:
    """Run ruff on notebook code and return any errors."""
    try:
        result = subprocess.run(
            ["ruff", "check", str(notebook_path), "--output-format=concise"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except FileNotFoundError:
        return ["ruff not found - install with: pip install ruff"]
    except subprocess.TimeoutExpired:
        return ["ruff check timed out"]
    if result.returncode != 0:
        return [
            line
            for line in result.stdout.strip().split("\n")
            if line and not line.startswith("Found")
        ]
    return []


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
            timeout=300,
            check=False,
        )
    except FileNotFoundError:
        return ["jupyter not found - install with: pip install jupyter"]
    except subprocess.TimeoutExpired:
        return ["Notebook execution timed out (>5 minutes)"]
    if result.returncode != 0:
        error_output = result.stderr.strip()
        if "AssertionError" in error_output:
            lines = error_output.split("\n")
            errors = [line for line in lines if "AssertionError" in line]
            return errors[:5] if errors else ["Assertion failed"]
    return []


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
            indent = len(line) - len(line.lstrip())
            result.append(" " * indent + "# your code here\n")
            continue
        if stripped == "# END SOLUTION":
            in_solution = False
            continue

        # Handle hidden test markers
        if stripped == "# BEGIN HIDDEN TESTS":
            in_hidden_tests = True
            continue
        if stripped == "# END HIDDEN TESTS":
            in_hidden_tests = False
            continue

        # Skip lines inside solution or hidden test blocks
        if in_solution or in_hidden_tests:
            continue

        # Handle inline solution marker (must end with # SOLUTION)
        if line.rstrip().endswith("# SOLUTION"):
            indent = len(line) - len(line.lstrip())
            # Extract variable name if there's an assignment (not ==, !=, <=, >=)
            code_part = line.split("# SOLUTION")[0].rstrip()
            # Match assignment: var = value (but not ==, !=, <=, >=)
            assign_match = re.match(r"^(\s*)([^=!<>]+)\s*=[^=]", code_part)
            if assign_match:
                var_name = assign_match.group(2).rstrip()
                result.append(" " * indent + var_name + " = ...  # your code here\n")
            else:
                result.append(" " * indent + "# your code here\n")
            continue

        result.append(line)

    # Remove trailing empty lines
    while result and result[-1].strip() == "":
        result.pop()

    # Remove trailing newline from last line
    if result and result[-1].endswith("\n"):
        result[-1] = result[-1][:-1]

    return result


def process_notebook(input_path: Path, output_dir: Path) -> tuple[Path, int, int]:
    """Process a notebook and write the student version."""
    with input_path.open() as f:
        nb = json.load(f)

    solutions_stripped = 0
    hidden_tests_stripped = 0

    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            # Clear outputs and execution count for student version
            cell["outputs"] = []
            cell["execution_count"] = None

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


def print_validation_result(result: ValidationResult) -> bool:
    """Print validation results and return True if valid."""
    print(f"\n{result.notebook_path}")
    print("=" * 60)

    all_valid = True

    if not result.problems:
        print("  No problems found in notebook")
        return False

    for problem in result.problems:
        suffix = " (free response)" if problem.is_free_response else ""
        print(f"  Problem {problem.number}: {problem.title}{suffix}")

        missing = []
        if not problem.has_prompt:
            missing.append("prompt cell")
        if not problem.has_solution:
            missing.append("solution cell")
        if not problem.has_tests and not problem.is_free_response:
            missing.append("test cell")

        if missing:
            print(f"    MISSING: {', '.join(missing)}")
            all_valid = False

        if problem.errors:
            for error in problem.errors:
                print(f"    ERROR: {error}")
            all_valid = False

        if not missing and not problem.errors:
            print("    OK")

    if result.ruff_errors:
        print("\n  Ruff errors:")
        for error in result.ruff_errors[:10]:
            print(f"    {error}")
        if len(result.ruff_errors) > 10:
            print(f"    ... and {len(result.ruff_errors) - 10} more")
        all_valid = False
    else:
        print("\n  Ruff: OK")

    if result.execution_errors:
        print("\n  Execution errors:")
        for error in result.execution_errors[:5]:
            print(f"    {error}")
        all_valid = False
    else:
        print("  Execution: OK")

    return all_valid


def main() -> None:
    """Validate notebook and create student version."""
    if len(sys.argv) != 2:
        print("Usage: python make_student_version.py <notebook.ipynb>")
        sys.exit(1)

    notebook_path = Path(sys.argv[1])

    if not notebook_path.exists():
        print(f"Error: {notebook_path} not found")
        sys.exit(1)

    if notebook_path.suffix != ".ipynb":
        print(f"Error: {notebook_path} is not a Jupyter notebook")
        sys.exit(1)

    # Validate the notebook
    result = validate_notebook(notebook_path, check_ruff=True, check_execution=True)
    is_valid = print_validation_result(result)

    if not is_valid:
        print("\nValidation failed. Fix issues before releasing.")
        sys.exit(1)

    # Create student version
    output_dir = Path("student")
    output_file, sol_count, hidden_count = process_notebook(notebook_path, output_dir)

    print(f"\nCreated: {output_file}")
    print(f"  {sol_count} solution(s) stripped")
    print(f"  {hidden_count} hidden test(s) stripped")


if __name__ == "__main__":
    main()
