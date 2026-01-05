---
## Critique: DATASCI 315, Group Work 3: Logistic Regression and Maximum Likelihood

### Summary
- **Critical issues**: 3
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Missing Problem 4**
   - **Location**: Between Problem 3 (cell-10) and Problem 5 (cell-24)
   - **Description**: The assignment jumps from Problem 3 to Problem 5, with no Problem 4 defined. The section titled "Introduction to Logistic Regression" appears where Problem 4 should be.
   - **Why problematic**: Students will be confused about whether there is a missing problem or if they need to complete something. This also breaks numbering conventions and could cause issues with autograding systems that expect sequential problem numbers.
   - **Suggested fix**: Either add Problem 4 (perhaps asking students to analyze the confusion matrix or interpret the sklearn model output) or renumber Problem 5 and 6 to be Problem 4 and 5.

2. **Placeholder Hidden Tests Throughout**
   - **Location**: All test cells (cells 4, 7, 10, 27, 30)
   - **Description**: All hidden test sections contain only `assert True  # placeholder hidden test`, which provides no actual verification of student solutions.
   - **Why problematic**: Without meaningful hidden tests, students could submit solutions that pass visible tests but fail on edge cases. The autograder will not catch incorrect implementations that happen to pass the visible tests.
   - **Suggested fix**: Add substantive hidden tests for each problem:
     - Problem 1: Test with p=0, p=1, and intermediate values
     - Problem 2: Test with all-zeros, all-ones, and mixed labels
     - Problem 3: Test numerical stability with very small/large probabilities
     - Problem 5: Test with different weight vector shapes, edge cases
     - Problem 6: Test convergence with different learning rates

3. **Sigmoid Function Missing Numerical Stability**
   - **Location**: Problem 5 (cell-26) and its usage in Problem 6
   - **Description**: The sigmoid implementation `1 / (1 + torch.exp(-z))` can produce NaN or Inf values for large positive or negative z values due to exp overflow.
   - **Why problematic**: Students may encounter numerical issues when running gradient descent, leading to NaN losses and confusion about why their implementation fails.
   - **Suggested fix**: Either (a) mention this is a simplified implementation and data should be standardized, or (b) teach the numerically stable form: `torch.sigmoid()` or implement stable version with `torch.where(z >= 0, 1/(1+exp(-z)), exp(z)/(1+exp(z)))`.

### Moderate Issues

1. **Inconsistent Requirement About Intercept**
   - **Location**: Problem 5 (cell-24) and Problem 6 (cell-28)
   - **Description**: Problem 5 states "Assume the intercept vector is already included in X" but Problem 6's solution adds the intercept column inside the function. The test for Problem 6 passes `initial_w` with shape `(p+1, 1)` expecting the function to handle intercept internally.
   - **Suggestion**: Clarify whether students should add the intercept or expect it pre-added. Update Problem 5 or 6 to be consistent, and make the expectation explicit in the docstring.

2. **Test Values May Not Match Student Implementations**
   - **Location**: Problem 2 test cell (cell-7)
   - **Description**: The assertion `assert abs(likelihood - 0.000069919) < 1e-9` uses a very tight tolerance (1e-9) for a value that is the product of 20 floating-point operations.
   - **Suggestion**: Increase tolerance to 1e-6 or use relative tolerance to accommodate minor floating-point differences.

3. **Missing Documentation Links**
   - **Location**: Throughout the assignment
   - **Description**: No links to PyTorch documentation for `torch.prod()`, `torch.sum()`, `torch.log()`, `torch.exp()`, or matrix operations.
   - **Suggestion**: Add links to relevant PyTorch documentation, especially for tensor operations and broadcasting rules.

4. **Confusion Matrix Comment is Incorrect/Confusing**
   - **Location**: Cell-23
   - **Description**: The comment showing confusion matrix layout has confusing labels mixing "true" and "predicted" in ways that don't match standard conventions.
   - **Suggestion**: Use standard confusion matrix labeling or reference sklearn's documentation for the exact layout.

5. **Problem 6 Missing Return Type Specification**
   - **Location**: Cell-29 docstring
   - **Description**: The docstring says the function returns `loss : float` but the implementation returns `loss.item()`. The type could be clearer (it's a Python float, not a tensor).
   - **Suggestion**: Clarify return types in the docstring.

6. **No Hints for Matrix Formulation**
   - **Location**: Problem 5 and Problem 6
   - **Description**: Students need to implement matrix operations but receive no hints about the relationship between the formula notation and PyTorch operations (e.g., $w^Tx_i$ vs. `X @ w`).
   - **Suggestion**: Add a hint about how row vectors in X correspond to transposed x_i vectors in the mathematical notation.

### Minor Issues

- **Cell-21**: Text references "54% confidence" but this specific value isn't shown in the output display; the example shown may produce different values.
- **Cell-24**: LaTeX formatting could use `\widehat` consistently (currently mixes display styles).
- **Cell-28**: The gradient formula shows the average (1/n factor) but the loss definition already includes this; could be clearer about why both have 1/n.
- **Problem headers**: Problems 5 and 6 use `## Problem N:` format instead of `### Problem N:` as specified in CLAUDE.md guidelines.
- **Cell-12**: Import of `load_breast_cancer` is repeated in cell-25; could consolidate imports.

### Strengths

1. **Clear Mathematical Foundation**: The assignment builds logically from Bernoulli distributions to likelihood to log-likelihood to logistic regression, providing a solid theoretical foundation.

2. **Good Use of Real Data**: The Wisconsin Breast Cancer dataset is a classic, well-understood dataset appropriate for teaching logistic regression.

3. **Vectorization Emphasis**: The explicit requirement to use broadcasting and avoid for loops teaches important practical skills for efficient computation.

4. **Progressive Complexity**: Problems build on each other appropriately, with earlier functions (bernoulli_distribution, sigmoid) used in later problems.

5. **Practical Context**: The assignment connects mathematical concepts to real-world application (tumor classification) and shows both hard and soft predictions.

6. **Good Test Coverage for Visible Tests**: Visible tests check multiple cases and include descriptive error messages.

### Recommendations

1. **Fix the missing Problem 4**: Either add a meaningful problem in the sklearn logistic regression section (e.g., interpreting coefficients, computing accuracy) or renumber subsequent problems.

2. **Add substantive hidden tests**: Replace placeholder assertions with real edge case tests that verify correct implementation without giving away solutions.

3. **Clarify intercept handling**: Make the convention consistent across Problems 5 and 6, and explicitly document whether students should add intercept columns or expect them pre-added.
---
