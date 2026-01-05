---
## Critique: Homework 3 - Gradient Descent and Linear Regression

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

#### 1. Missing Data File Path Specification
**Location:** Problem 4, cell-21
**Description:** The code reads from `"data/housing.csv"` but students are not told where this file should be located, whether it's provided, or how to obtain it.
**Why problematic:** Students cannot run Problem 4 and 5 without this data file. The assignment will fail immediately at this cell if the file is missing.
**Suggested fix:** Either include a cell that downloads the dataset (e.g., from sklearn's `fetch_california_housing`) or add a clear note about where to find/download the data file. Consider using the built-in sklearn dataset loader for reproducibility.

#### 2. Inconsistent Convergence Criteria Between Problems
**Location:** Problems 1-5
**Description:** Different problems use different convergence criteria:
- Problem 1: `abs(w - old_w)` (absolute difference of scalar)
- Problem 2: `torch.sum(torch.abs(w - old_w))` (L1 norm)
- Problems 3, 4, 5: `||w_k - w_{k-1}||_infinity` (infinity norm)

**Why problematic:** Students may not realize these are different norms and why. The solution for Problem 2 uses L1 norm but the problem doesn't specify which norm to use. This inconsistency can confuse students about which convergence criterion to use.
**Suggested fix:** Explicitly state the convergence criterion in Problem 2 (recommend infinity norm for consistency) and add a brief note explaining why infinity norm is a common choice.

### Moderate Issues

#### 1. Missing Return Type Specification in Problem 2
**Location:** Problem 2 (cell-8)
**Description:** The problem says "return the final values of $w_1$ and $w_2$" but doesn't specify the return format (tuple, list, tensor, etc.).
**Suggestion:** Clarify that the function should return a tuple `(w1, w2)` of floats/numbers.

#### 2. Weak Visible Tests in Problem 2
**Location:** Cell-10
**Description:** The visible tests only check that values are within 0.5 of the true minimum. Given the Rosenbrock function's notoriously challenging optimization landscape, this is quite lenient and doesn't verify the algorithm is actually working correctly.
**Suggestion:** Add a test that verifies the loss is decreasing or that the final function value is small (e.g., `f(w1, w2) < 0.1`).

#### 3. Missing Type Hints and Docstrings
**Location:** All problem function definitions
**Description:** Functions lack type hints and detailed docstrings explaining input/output types and shapes.
**Suggestion:** Add type hints (e.g., `def problem3(x: torch.Tensor, y: torch.Tensor, ...) -> tuple[float, float]:`) and expand docstrings to document parameter types and return types.

#### 4. No Guidance on Numerical Stability
**Location:** Problems 3-5
**Description:** Students implementing gradient descent may encounter numerical issues (overflow, underflow) but no guidance is provided.
**Suggestion:** Add a note about using float32/float64 and the importance of feature scaling (which is done in the test code but not explained).

#### 5. Problem 5 Terminology Inconsistency
**Location:** Cell-25 and cell-26
**Description:** The problem uses "iteration" in the algorithm description but the test code plots "Epoch". These are different concepts (an epoch is one pass through all batches; an iteration is one batch update).
**Suggestion:** Clarify that the outer loop represents epochs and each inner loop iteration is a batch update. Update the algorithm description to use "epoch" terminology consistently.

### Minor Issues

- **Cell-8 (Problem 2):** Hint 1 mentions "NumPy array" but the solution uses PyTorch tensors. Should say "torch tensor" for consistency with the imports.

- **Cell-12 (Problem 3):** The problem provides gradients but doesn't explain the derivation. Adding a brief note like "You can derive these by applying the chain rule" would be pedagogically helpful.

- **Cell-17:** The test prints sklearn results before the student's solution runs, which could confuse students about output ordering.

- **Cell-18 (Problem 4):** The loss history stores the loss before convergence check, meaning the first loss in the list is after the first weight update. This is fine but could be clearer.

- **Cell-23 (Problem 5):** The formula shows $|B_j|$ for batch size but uses $|B|$ for input batch size. The notation is slightly inconsistent (should clarify that $|B_j|$ may differ from $|B|$ for the last batch).

- **Cell-3:** Missing `import numpy as np` even though numpy could be useful for students (and is referenced in Hint 1 of Problem 2).

### Strengths

1. **Excellent scaffolding:** The assignment builds progressively from a simple 1D function to 2D, then to simple linear regression, multivariate regression, and finally minibatch gradient descent.

2. **Good use of hints:** Each problem provides helpful hints including gradient formulas, which allows students to focus on the algorithm implementation rather than calculus.

3. **Real-world dataset:** Using the California Housing dataset in Problems 4-5 gives students practical experience with a real dataset.

4. **Comparison with sklearn:** Providing sklearn baselines helps students verify their implementations and understand that gradient descent approaches the same solution as closed-form methods.

5. **Visualization:** Including loss curve plots helps students understand the optimization process and verify convergence.

6. **Clear mathematical notation:** The assignment uses consistent LaTeX notation for equations and clearly defines all variables.

### Recommendations

1. **Fix the data file issue (Critical):** Either use `sklearn.datasets.fetch_california_housing()` or provide clear instructions on obtaining the `housing.csv` file. This is blocking for students attempting Problems 4-5.

2. **Standardize convergence criteria:** Use infinity norm consistently across all problems and add a brief explanation of why this norm is chosen.

3. **Add type hints and improve docstrings:** This helps students understand expected inputs/outputs and is good software engineering practice.

---
