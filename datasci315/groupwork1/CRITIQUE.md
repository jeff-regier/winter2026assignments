---
## Critique: DATASCI 315, Group Work 1: PyTorch Tensor Operations and Matplotlib

### Summary
- **Critical issues**: 2
- **Moderate issues**: 7
- **Minor issues**: 8

### Critical Issues

#### 1. Typo in Variable Initialization (Cell 116)
**Location:** Cell 116, line defining `b`
**Description:** The code has `b = torch.tensor([3 - 1, 2, 1], ...)` which creates `[2, 2, 1]` instead of the intended `[-1, 2, 1]` shown in the mathematical notation above.
**Why problematic:** This is a factual error that will confuse students. The displayed matrix shows `b = (-1, 2, 1)^T` but the code computes something different. Students may not notice this discrepancy and will be confused when trying to verify results.
**Suggested fix:** Change to `b = torch.tensor([-1, 2, 1], dtype=torch.float32)`

#### 2. Problem 12 Hidden Tests Appear After print Statement
**Location:** Cell 152
**Description:** The hidden tests block appears after `print("All tests passed!")`, which violates the test cell structure convention.
**Why problematic:** The hidden tests should be before the print statement so that if hidden tests fail, "All tests passed!" is not misleadingly printed.
**Suggested fix:** Move the `# BEGIN HIDDEN TESTS` block before `print("All tests passed!")`

### Moderate Issues

#### 1. Inconsistent Print Statement in Test Cell
**Location:** Cell 106
**Description:** Uses `print("All assertions passed!")` instead of the standard `print("All tests passed!")`.
**Suggestion:** Change to `print("All tests passed!")` for consistency with other test cells.

#### 2. Problem 8 Has Weak Tests
**Location:** Cell 132
**Description:** The test only checks that `y` has the same length as `x` and that `y.min() >= 0`. It does not verify that the formula `x^2 - 2x + 1` was actually used. The hidden tests are identical to visible tests, providing no additional validation.
**Suggestion:** Add tests that verify specific values, e.g., `assert torch.isclose(y[x == 1].item(), 0.0)` to check that the minimum is at x=1.

#### 3. Problem 9 Has Minimal Tests
**Location:** Cell 142
**Description:** The test only checks that `ax.shape == (2, 2)` and that the top-left subplot has a title. It does not verify that all four functions (sine, cosine, x^2, x) are plotted or that all subplots have titles.
**Suggestion:** Add hidden tests to verify all four subplots have non-empty titles and that each contains plotted data.

#### 4. Missing Documentation Link for Matplotlib
**Location:** Cells 120-145 (Matplotlib section)
**Description:** The PyTorch section has excellent documentation links, but the Matplotlib section only links to the subplot documentation. Students would benefit from a link to the main matplotlib tutorial or pyplot documentation.
**Suggestion:** Add link: "See the [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) for more details."

#### 5. Problem 6 Could Use Better Scaffolding
**Location:** Cell 110
**Description:** This is a complex multi-part problem involving tensor broadcasting, permutation, and reduction. The hint mentions `torch.arange` but does not explain how to construct the three different k-channel expressions using broadcasting.
**Suggestion:** Add a worked example showing how to construct a simpler 2D tensor using broadcasting with indices, or break the problem into more explicit sub-steps.

#### 6. Problem 11 Missing Return Type Specification
**Location:** Cell 146-148
**Description:** The problem statement says "Return a rank-1 tensor of the same length as `x_test`" but the docstring is missing from the function template.
**Suggestion:** Add a docstring template with parameter types and return type to the function skeleton.

#### 7. Problem 3 Has Potentially Confusing Test Structure
**Location:** Cells 83-84
**Description:** The comment explaining Cayley-Hamilton theorem appears in the solution cell (83) rather than in the problem statement or test cell. Also, the `expected` variable is defined in the solution cell but the assertion is in the test cell.
**Suggestion:** Move the `expected` tensor definition to the test cell, and consider moving the Cayley-Hamilton explanation to the problem statement as educational context.

### Minor Issues

- **Cell 17:** "Note: Detailed documentation for PyTorch" would read better as "For detailed documentation, see the PyTorch docs."
- **Cell 42:** Problem 1 hint says "Use `torch.arange` with appropriate start and stop values" but students also need the step parameter for the slicing, which could be clarified.
- **Cell 60:** The math rendering uses `$$ ... $$` which may not render in all Jupyter environments. Consider using single `$` for inline math or ensuring LaTeX is properly configured.
- **Cell 82:** The expected output code block shows `tensor([[0., 0.],` but the actual output may show `tensor([[0, 0],` depending on dtype display settings.
- **Cell 117:** "Expected output:" section shows specific tensor formatting that may differ slightly across PyTorch versions.
- **Cell 130:** Problem 8 is very simple (one line of code) and could be combined with another plotting problem for better pacing.
- **Cell 146:** The kernel smoothing formula uses `$	ext{...}$` which should be `$\text{...}$` (missing backslash in LaTeX).
- **Cell 150:** Same LaTeX issue with `$	ext{LeastSquares}$`.

### Strengths

1. **Excellent progressive structure:** The assignment builds from basic tensor creation to advanced broadcasting and finally to practical applications (activation functions, kernel smoothing).

2. **Comprehensive coverage of indexing:** The tutorial thoroughly covers slicing, integer indexing, and boolean indexing with clear examples.

3. **Good use of practical examples:** The pairwise Euclidean distance example effectively demonstrates real-world broadcasting usage.

4. **Well-designed problems:** Problems like the activation functions (Problem 7) and kernel smoothing (Problem 11) connect to machine learning concepts students will use later.

5. **Consistent formatting:** Problem headers, solution markers, and test cells follow the conventions well throughout.

6. **Helpful hints:** Most problems include useful hints with specific function references and approaches.

7. **Good documentation links:** PyTorch documentation is well-referenced throughout the tensor operations section.

8. **Hidden tests present:** All problems have hidden tests for autograding, which is good for academic integrity.

### Recommendations

1. **Fix the critical typo in Cell 116** where `b = torch.tensor([3 - 1, 2, 1], ...)` should be `b = torch.tensor([-1, 2, 1], ...)` to match the displayed mathematical notation.

2. **Strengthen test cases for plotting problems (8, 9, 10)** by adding hidden tests that verify specific values or properties of the plotted data, not just shape checks.

3. **Add Matplotlib documentation link** at the start of the plotting section to match the quality of documentation references in the PyTorch section.
---
