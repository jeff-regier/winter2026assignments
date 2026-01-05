---
## Critique: DATASCI 503, Group Work 8: Support Vector Machines

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

1. **Variable Overwriting Creates Hidden Dependencies**
   - **Location**: Problems 6-9 (cells 41 onwards)
   - **Description**: Problem 6 overwrites `X` and `y` with new data from `make_circles`, destroying the data from Problem 1. This means Problems 3-5 results are lost, and if a student runs cells out of order, they will get confusing errors.
   - **Why problematic**: Students debugging or re-running earlier problems will encounter failures because the global `X` and `y` have been silently replaced. This creates confusion and makes the notebook non-idempotent.
   - **Suggested fix**: Use distinct variable names like `X_blobs, y_blobs` for Problem 1 data and `X_circles, y_circles` for Problem 6 data. Update all downstream references accordingly.

2. **Test Cell Potentially Gives Away Solution in Problem 8**
   - **Location**: Cell 52
   - **Description**: The assertion `assert poly_accuracy == lin_feature_accuracy, "Both methods should give same accuracy"` combined with `assert poly_accuracy >= 0.9` tells students exactly what outcome to expect, potentially allowing them to reverse-engineer the solution.
   - **Why problematic**: Students can determine that `gamma=1` is needed for the polynomial SVM (since the problem asks them to verify equivalence). The test essentially gives away that the accuracies must match exactly, which is a key learning point that should be discovered, not given.
   - **Suggested fix**: Move the equality assertion to hidden tests. The visible test should only check that both models are fitted and produce reasonable outputs.

### Moderate Issues

1. **Missing Random State Specification in Problems 3 and 7**
   - **Location**: Cells 29, 45
   - **Description**: Problems 3 and 7 require `train_test_split` but do not specify what `random_state` to use in the problem statement. The solution uses `random_state=503` but this is not mentioned in the instructions.
   - **Suggestion**: Either explicitly state `random_state=503` in the problem text, or remove the hidden test that depends on exact split results.

2. **Problem 7 Solution Inconsistent with Problem 4**
   - **Location**: Cell 45
   - **Description**: Problem 4 asks for black dashed margin lines (`k-.`), but the solution in Problem 7 uses red dashed lines (`r-.`) for margins. This inconsistency may confuse students.
   - **Suggestion**: Update Problem 7 instructions to specify the color scheme, or update the solution to match Problem 4's convention.

3. **Missing Scaffolding for Problem 8**
   - **Location**: Cell 48
   - **Description**: Problem 8 jumps into polynomial kernels and feature mappings without sufficient explanation of why `gamma=1` is needed for the polynomial SVM to match the explicit feature mapping.
   - **Suggestion**: Add a hint explaining that `gamma=1` is required for the kernel to match the explicit feature mapping, or provide the sklearn documentation link explaining kernel parameters.

4. **Problem 9 Outline Missing Critical Detail**
   - **Location**: Cell 54
   - **Description**: The outline mentions using `svc.decision_function` but doesn't clarify that students need to use `poly_svm` and `lin_feature_svm` (variables defined in the previous cell). Also doesn't explain what `levels=[0]` means in `plt.contour`.
   - **Suggestion**: Be explicit about which variable names to use, and briefly explain that `levels=[0]` plots the decision boundary where the decision function equals zero.

5. **Problem 2 Test is Too Weak**
   - **Location**: Cell 26
   - **Description**: The test only checks that `colors` exists, has the correct length, and contains valid colors. It doesn't verify that the mapping is correct (orange for 0, skyblue for 1).
   - **Suggestion**: Add a hidden test that verifies `colors[i]` matches `y[i]` correctly.

6. **Visualization Problems Lack Testability**
   - **Location**: Problems 2, 4, 7, 9
   - **Description**: Visualization problems are inherently hard to test. The current tests only check intermediate variables, not the actual plot output.
   - **Suggestion**: Consider adding `plt.gcf()` or `plt.gca()` checks, or explicitly require students to save certain intermediate values that can be tested.

### Minor Issues

- **Cell 12**: Typo "metrices" should be "metrics"
- **Cell 14**: Typo "cros-validated" should be "cross-validated"
- **Cell 17**: GitHub link may become stale; consider archiving or removing
- **Cell 20**: The term "quasi-linearly separable" is not standard terminology; consider "approximately linearly separable"
- **Cell 32**: Uses `$w_1 x_1 + w_2 x_2 + b = 0$` but should clarify this is the equation solved for the decision boundary line
- **Cell 36**: "within the margins" could be clarified as "points with decision function magnitude less than 1"
- **Problem header inconsistency**: Some problems have colons after the number, all should be consistent
- **Cell 52**: The test `assert poly_accuracy == lin_feature_accuracy` may fail due to floating-point differences; consider using `np.isclose`

### Strengths

1. **Excellent pedagogical progression**: The assignment builds logically from linear SVMs to kernel methods, demonstrating the kernel trick with a concrete example.
2. **Good use of visualization**: Multiple problems require students to visualize decision boundaries, which reinforces understanding of SVM geometry.
3. **Appropriate complexity**: The problems are well-scoped for a group work assignment, covering key SVM concepts without being overwhelming.
4. **Clear mathematical notation**: The quadratic feature transformation is clearly specified with proper mathematical notation.
5. **Good real-world motivation**: Starting with the iris dataset in the overview provides context before moving to synthetic examples.
6. **Hidden tests are appropriate**: Most hidden tests check edge cases and specific values without giving away solutions (with the exception noted above).

### Recommendations

1. **Fix variable overwriting (Critical)**: Rename `X, y` in Problems 1 and 6 to use distinct names (`X_blobs`, `X_circles`, etc.) to prevent confusion and allow non-linear execution.

2. **Add missing parameters to problem statements**: Explicitly state `random_state=503` in Problems 3 and 7, and add `gamma=1` hint to Problem 8 with a brief explanation of why it matters.

3. **Strengthen tests for visualization problems**: Add hidden tests that verify the color mapping is correct in Problem 2, and consider checking plot axis labels or other testable properties in later visualization problems.
---
