---
## Critique: Homework 4 - Multiclass Logistic Regression

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

1. **Inconsistent library requirement (NumPy vs PyTorch)**
   - **Location**: Problem 2 (cell 8) and Problem 4 (cell 14)
   - **Description**: The requirement states "Use only NumPy functions" but the entire assignment uses PyTorch tensors. The solution and test cells all use `torch` operations.
   - **Why problematic**: Students will be confused about which library to use. The assignment loads PyTorch, creates PyTorch tensors, and the solution uses PyTorch, yet the instructions say "NumPy." This is a direct contradiction.
   - **Suggested fix**: Change "Use only NumPy functions (not SciPy)" to "Use only PyTorch tensor operations" in both Problem 2 and Problem 4.

2. **Hardcoded number of classes in lr_train**
   - **Location**: Problem 4 (cell 15, solution)
   - **Description**: The solution hardcodes `torch.arange(3)` for the labels, which assumes exactly 3 classes.
   - **Why problematic**: This makes the function non-generalizable and will fail silently or produce incorrect results for datasets with more or fewer classes. Students may copy this pattern thinking it's correct.
   - **Suggested fix**: Either pass the labels/number of classes as a parameter, or derive them from `y` using `torch.unique(y)`.

### Moderate Issues

1. **Missing hint alternative in Problem 1**
   - **Location**: Problem 1 (cell 5)
   - **Description**: The hint suggests using `torch.nn.functional.one_hot` directly, but then the requirements prohibit loops. If students use the built-in function, the exercise becomes trivial. The pedagogical goal is unclear.
   - **Suggestion**: Either remove the hint about `torch.nn.functional.one_hot` to ensure students learn the underlying logic, or explicitly state whether using the built-in is acceptable for full credit.

2. **Numerical stability issue not addressed in lr_predict**
   - **Location**: Problem 2 (cell 9)
   - **Description**: The naive softmax implementation in `lr_predict` can overflow when inputs are large. The standard practice is to subtract the maximum value before exponentiating.
   - **Suggestion**: Either mention this limitation and say Problem 3 addresses it, or require a stable implementation. At minimum, add a note explaining why Problem 3 is needed.

3. **Test cell uses undefined variable `labels`**
   - **Location**: Problem 4 test cell (cell 16)
   - **Description**: The test cell references `m` which was defined using `labels.shape[0]` in cell 10. If students run cells out of order or restart the kernel, this will fail confusingly.
   - **Suggestion**: Define `m = 3` explicitly in the test cell, or compute it from `torch.unique(y_train_iris)`.

4. **Loss bounds in tests may be fragile**
   - **Location**: Problem 4 test cell (cell 16)
   - **Description**: The assertions `assert training_loss < 15` and `assert training_loss > 5` are magic numbers without justification. Different initializations or learning rates could produce valid but out-of-range values.
   - **Suggestion**: Add comments explaining why these bounds are reasonable, or use more robust checks like "loss should decrease from initial loss."

5. **No documentation links for key concepts**
   - **Location**: Problems 2 and 3
   - **Description**: While the softmax and logsumexp functions are explained mathematically, there are no links to PyTorch documentation or external resources for students who want deeper understanding.
   - **Suggestion**: Add links to `torch.nn.functional.softmax` and `torch.logsumexp` documentation pages.

### Minor Issues

- **Problem 1**: The example uses names (Sahana, Eduardo, Jake) but the actual exercise uses numeric labels. Consider using numeric labels in the example for consistency.
- **Problem 1**: Parameter name inconsistency: function signature uses `labels` but description uses `l`.
- **Problem 2**: The equation uses $W$ as an $m \times p$ matrix but could clarify that rows correspond to classes.
- **Problem 3**: The assertion message "exp(log_probs) should sum to 1" could be more descriptive about what went wrong.
- **Cell 4**: Comment says "this part loads the iris dataset" - could be more descriptive about what preprocessing is happening (especially the intercept addition).
- **Formatting**: Problem 2 uses "NumPy" but should say "PyTorch" to match the actual library being used.

### Strengths

1. **Clear mathematical exposition**: Each problem provides the mathematical foundation with well-formatted LaTeX equations before asking students to implement.

2. **Logical progression**: The assignment builds naturally from one-hot encoding to prediction to numerically stable prediction to training, each building on the previous.

3. **Good worked example**: The one-hot encoding example with names is intuitive and helps students understand the concept before implementing.

4. **Appropriate difficulty scaffolding**: Starting with encoding, then forward pass, then stable forward pass, then full training loop is a sensible pedagogical sequence.

5. **Meaningful hidden tests**: The hidden tests check edge cases (extreme values for numerical stability, accuracy thresholds) that go beyond the visible tests.

6. **Proper test cell structure**: All test cells follow the required format with first line comment, visible assertions, success message, and hidden tests section.

### Recommendations

**Top 3 Priority Fixes:**

1. **Fix the NumPy/PyTorch inconsistency** - This is causing immediate confusion. Change all references from "NumPy" to "PyTorch" in Problems 2 and 4.

2. **Fix the hardcoded class count in lr_train** - Either add a `labels` parameter to the function signature, or compute labels from `torch.unique(y)` in the solution. Update the docstring accordingly.

3. **Clarify the hint in Problem 1** - Either remove the hint about `torch.nn.functional.one_hot` or explicitly state that using it is acceptable. The current wording is ambiguous about expectations.
---
