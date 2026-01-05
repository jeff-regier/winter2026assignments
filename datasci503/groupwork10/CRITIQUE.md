---
## Critique: DATASCI 503, Group Work 10: Stochastic Gradient Descent for Loss Functions

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

#### 1. Solution Bug in Problem 3 (Simultaneous vs Sequential Update)
**Location:** Cell 18, `simple_linear_regression_gd` function

**Description:** The solution uses `alpha_prev` instead of `alpha` when computing the beta gradient, implementing a form of sequential (Gauss-Seidel) update rather than simultaneous gradient descent:
```python
alpha = alpha - eta * grad_alpha(alpha, beta)
beta = beta - eta * grad_beta(alpha_prev, beta_prev)  # Should use alpha, beta
```

**Why problematic:** This is mathematically incorrect for standard gradient descent, which should compute both gradients at the same point before updating. While this may still converge, it teaches students the wrong algorithm and could cause confusion when compared to the theoretical description.

**Suggested fix:** Compute both gradients before updating either parameter:
```python
grad_a = grad_alpha(alpha, beta)
grad_b = grad_beta(alpha, beta)
alpha = alpha - eta * grad_a
beta = beta - eta * grad_b
```

#### 2. Convergence Condition Bug in Problem 3
**Location:** Cell 18, convergence check

**Description:** The convergence check requires BOTH conditions to be met (`param_change < epsilon and loss_change < epsilon`), but on the first iteration, `w_prev` is `inf` so `param_change` will be `inf`. This means the function relies on the `loss_change` condition alone initially, which is inconsistent with the documented behavior stating "either" condition should suffice.

**Why problematic:** The behavior differs from what is stated in the problem description (Cell 17), which says "either of two ways" should work. The implementation requires both, creating a discrepancy between documentation and implementation.

**Suggested fix:** Change the condition to use `or` instead of `and`, or update the documentation to match the implementation.

### Moderate Issues

#### 1. Title Mismatch: "Stochastic" vs "Minibatch" Gradient Descent
**Location:** Title (Cell 0)

**Description:** The assignment title mentions "Stochastic Gradient Descent" but Problem 5 implements minibatch gradient descent. True SGD uses batch_size=1.

**Suggestion:** Either rename to "Gradient Descent Methods for Loss Functions" or add a problem that specifically implements SGD with batch_size=1 and discusses the difference.

#### 2. Missing Mathematical Derivation for Gradients
**Location:** Problems 1-3

**Description:** Students are expected to implement gradient descent but the gradients are not derived or explained. Problem 2 includes partial gradients in comments in the solution but these are hidden from students.

**Suggestion:** Add a brief derivation of the gradient for each function, or at minimum provide the gradient formula explicitly:
- Problem 1: State that the gradient of $f(w) = (w-2)^2$ is $f'(w) = 2(w-2)$
- Problem 2: Provide the Rosenbrock gradient formulas
- Problem 3: Show the derivation of $\partial L/\partial \alpha$ and $\partial L/\partial \beta$

#### 3. Inconsistent Convergence Criteria Across Problems
**Location:** Problems 1-5

**Description:** Different problems use different convergence criteria:
- Problem 1: Parameter change only
- Problem 2: Parameter change only (L2 norm)
- Problem 3: Both parameter AND loss change
- Problem 4: Both parameter AND loss change
- Problem 5: Parameter change only (L1 norm)

**Suggestion:** Standardize the convergence criteria across problems or explicitly discuss why different criteria are used in different contexts.

#### 4. No Maximum Iteration Limit
**Location:** All gradient descent implementations

**Description:** None of the gradient descent functions include a maximum iteration limit. With poor learning rate choices or edge cases, these functions could run indefinitely.

**Suggestion:** Add a `max_iterations` parameter with a reasonable default (e.g., 10000) and return the current weights if exceeded, possibly with a warning.

#### 5. Test Cells Depend on Prior Cell Execution Order
**Location:** Cells 30-33, 42-45

**Description:** The test cells for Problems 4 and 5 rely on variables defined in earlier cells (e.g., `X_train_scaled`, `lr_multi`, `sklearn_train_loss`). If students run cells out of order, tests will fail with confusing errors.

**Suggestion:** Make each test cell self-contained by including necessary setup, or add a note warning students about cell execution order.

### Minor Issues

- **Problem 2 hint is vague:** The hint "You can treat $w$ as a vector, but this is not necessary" doesn't help students understand the approach. Consider providing more specific guidance.

- **Inconsistent norm usage:** Problem 2 uses L2 norm, Problem 5 uses L1 norm for convergence checking. This inconsistency should be explained or standardized.

- **Cell 6 typo:** Uses `$w\star$` which doesn't render correctly in Markdown. Should be `$w^*$` or `$w^\star$`.

- **Missing type hints consistency:** Some functions have full type hints while starter code could benefit from showing expected shapes more clearly.

- **Problem 4 note about intercept column:** The note says the function "should automatically add a column of ones" but doesn't explain why this is needed or how it relates to the intercept term.

- **No learning rate guidance:** While Problem 2 mentions adjusting the learning rate, there's no guidance on how to choose appropriate learning rates for different problems.

### Strengths

1. **Clear progression of difficulty:** The assignment builds naturally from 1D optimization to 2D, then to linear regression with increasing complexity (simple to multivariate to minibatch).

2. **Good use of real-world data:** Using the California Housing dataset in later problems provides practical context and meaningful validation.

3. **Helpful comparison with sklearn:** Providing sklearn comparisons gives students a ground truth to validate their implementations.

4. **Well-structured test cells:** Tests include both visible assertions with descriptive messages and hidden tests for autograding.

5. **Clear algorithm descriptions:** The minibatch gradient descent algorithm is presented step-by-step in a clear, formal manner.

6. **Practical hints:** The shuffle hint in Problem 5 provides useful starter code for handling batch creation.

7. **Good documentation:** Function docstrings clearly specify input/output types and meanings.

### Recommendations

1. **Fix the solution bug in Problem 3:** The incorrect gradient update order is a critical error that teaches wrong concepts. This should be fixed immediately.

2. **Add explicit gradient formulas:** For an assignment focused on gradient descent, students need to see the gradient derivations or at minimum have the formulas provided. This is essential for understanding the algorithm.

3. **Standardize convergence criteria and add max iterations:** Using consistent stopping conditions across problems (or explaining the differences) would improve clarity. Adding a safety limit on iterations prevents infinite loops.

---
