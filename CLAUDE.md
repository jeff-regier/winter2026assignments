# CLAUDE.md

This repository contains course materials for DATASCI 315, including homework and groupwork Jupyter notebook assignments.

## Project Structure

- `homework*/` - Individual homework assignments (Jupyter notebooks)
- `groupwork*/` - Group work assignments (Jupyter notebooks)
- `student/` - Student versions of assignments (solutions stripped)
- `make_student_version.py` - Tool to validate and generate student versions

## Key Commands

```bash
# Run linting on a notebook
uv run ruff check <path/to/notebook.ipynb>

# Format a notebook
uv run ruff format <path/to/notebook.ipynb>

# Validate and generate student version (validates structure, runs ruff, executes notebook, then strips solutions)
uv run python make_student_version.py <path/to/notebook.ipynb>
```

## Assignment Conventions

### Solution Markers
- Block solutions: `# BEGIN SOLUTION` / `# END SOLUTION`
- Inline solutions: `variable = value  # SOLUTION`
- Free-response (markdown): Same markers in markdown cells for text-only answers

### Free-Response Problems
For problems requiring written explanations (no code), use solution markers in a markdown cell:
```markdown
### Problem N: Title

Question text here.
```
```markdown
# BEGIN SOLUTION
Your answer text here.
# END SOLUTION
```
The validator will recognize these as "(free response)" and won't require test cells.

### Test Cell Structure
1. First line must be: `# Test assertions`
2. Visible assertions with descriptive error messages
3. Print success message: `print("All tests passed!")`
4. Hidden tests section:
   ```python
   # BEGIN HIDDEN TESTS
   assert edge_case, "description"
   # END HIDDEN TESTS
   ```

### Cell Separation Rule
Solution code and test assertions must be in SEPARATE cells. Never put asserts in the same cell as `# BEGIN SOLUTION`.

### Problem Headers
Use `### Problem N: Title` or `#### Problem N: Title` (no bold, no point values).

### Assignment Title Format
`# DATASCI 315, [Assignment Type] [N]: [Topic]`

## Improving Assignments

Use `/improve-assignment <filepath>` to review and improve an assignment. This will:
- Check for ambiguities and unclear requirements
- Verify pedagogical quality (hints, worked examples, scaffolding)
- Fix grammar, formatting, and variable naming
- Solve all problems with clean, idiomatic code
- Add hidden tests for autograding
- Run ruff and structure validation

## Dependencies

Key libraries: torch, torchvision, torch-geometric, numpy, pandas, scikit-learn, scikit-image, matplotlib, networkx, transformers, datasets, tqdm, mnist1d, astropy, nltk

## Guidelines

- No single-letter variable names (except loop indices `i`, `j`, `k` or math conventions)
- Prefer library idioms (torch operations over loops for tensors)
- Keep solutions simple and educational
- Include worked examples for complex algorithmic problems
- Link to relevant documentation (Py4E chapters, official docs)
