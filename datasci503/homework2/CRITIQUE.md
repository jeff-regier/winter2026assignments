---
## Critique: DATASCI 503, Homework 2: K-Nearest Neighbors and Bias-Variance Tradeoff

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

1. **Inconsistent definition of squared Euclidean distance**
   - **Location**: Problem statement (cell 2) and Problem 1a
   - **Description**: The assignment defines squared Euclidean distance as $d(a, b) = \sum_{j=1}^{3}(a_j - b_j)^2$, but then the solution in Problem 1a computes distances using this formula directly. The issue is that "squared Euclidean distance" is used but when K-NN typically refers to "nearest neighbors," it uses regular Euclidean distance. While using squared distance preserves ordering, this should be clarified for students.
   - **Why problematic**: Students may be confused about whether K-NN uses squared or regular Euclidean distance in practice. More critically, if a student computes regular Euclidean distance (by taking square roots), their numeric answers will differ from the solution but their classification would still be correct.
   - **Suggested fix**: Either (1) explicitly state that squared distance is equivalent to regular distance for finding nearest neighbors since it preserves ordering, or (2) ask students to compute regular Euclidean distance to align with standard practice.

2. **Hidden test in Problem 3d contradicts problem setup**
   - **Location**: Cell 27, hidden test assertions
   - **Description**: The hidden test asserts `0.4 < np.mean(predictions) < 0.6`, but Problem 3e explicitly states the true value is $f(0.5) = -0.5$. The OLS model is intentionally biased because it fits a linear model to a nonlinear function. However, the expected mean prediction at $x=0.5$ for a linear OLS fit is indeed around 0.5 (not -0.5), which is correct. But the visible test in cell 30 asserts the same range, which gives away that the answer should be around 0.5.
   - **Why problematic**: The visible test in Problem 3e (`assert 0.4 < mean_prediction < 0.6`) essentially reveals the answer to students before they can reason about it themselves.
   - **Suggested fix**: Remove or widen the range in the visible test for Problem 3e. The hidden test can remain strict, but the visible test should not give away the numerical answer.

### Moderate Issues

1. **Missing documentation links for K-NN and sklearn**
   - **Location**: Throughout the assignment
   - **Description**: The assignment uses sklearn's LinearRegression but provides no links to documentation. No links to K-NN theory resources or the sklearn KNeighborsClassifier documentation are provided either.
   - **Suggestion**: Add links to sklearn documentation and relevant course materials or textbooks (e.g., ISL Chapter 2 for K-NN, sklearn LinearRegression documentation).

2. **Problem 3c lacks scaffolding for data generation**
   - **Location**: Cell 21-23
   - **Description**: Students must generate data from a conditional uniform distribution, which requires understanding that `np.random.uniform(low, high, size)` can accept arrays for `low` and `high`. This is not obvious and not hinted at.
   - **Suggestion**: Add a hint explaining that `np.random.uniform` can broadcast when given array bounds, or provide a partial code template showing the structure.

3. **Test assertions could reveal solution structure in Problem 3c**
   - **Location**: Cell 24
   - **Description**: The visible test checks `hasattr(ols_model, "coef_")`, which confirms the expected class of the model. While helpful, it could be more educational.
   - **Suggestion**: Consider adding a hint in the problem text that students should use `LinearRegression` from sklearn, rather than having them discover it through failing tests.

4. **Problem 3e visible test is too narrow**
   - **Location**: Cell 30
   - **Description**: The assertion `assert 0.4 < mean_prediction < 0.6` is too narrow and gives away the expected answer. Additionally, this test could theoretically fail due to random variation (though unlikely with 500 samples).
   - **Suggestion**: Widen the visible test range significantly (e.g., `0.0 < mean_prediction < 1.0`) and keep the stricter bounds in hidden tests only.

5. **Problem 3g redefines `estimator_variance` without warning**
   - **Location**: Cell 37
   - **Description**: The solution in Problem 3g recomputes `estimator_variance` from `predictions`, overwriting the value from Problem 3f. This could confuse students about variable scope and reuse.
   - **Suggestion**: Either instruct students to reuse the variable from 3f, or rename to avoid confusion. The test in cell 38 checks the value anyway, so consistency matters.

### Minor Issues

- **Problem headers use `###` consistently** but Problem 3 subproblems (3a-3g) would benefit from being numbered as 3.1, 3.2, etc. for clarity
- **Cell 22**: The comment "Define the true regression function" is in a setup cell that also imports libraries; consider separating imports from helper function definitions
- **Problem 1d**: The phrase "In a typical data-generating process" is somewhat vague - could specify "when the Bayes decision boundary is smooth" or similar
- **Problem 2a and 2b**: These are conceptual questions without code; while appropriate, they feel disconnected from the simulation study that follows
- **Cell 26 solution**: The histogram lacks a vertical line showing the true value $f(0.5) = -0.5$, which would make the bias visually apparent
- **Problem 3b**: The solution shows $\approx 0.00333$ but the exact value is $1/300$; consider showing the exact fraction

### Strengths

- **Excellent pedagogical flow**: The assignment builds from simple K-NN classification to a sophisticated bias-variance simulation study
- **Well-structured problems**: Each problem builds on previous ones, reinforcing learning
- **Clear mathematical notation**: LaTeX is used consistently and correctly throughout
- **Good balance of theory and practice**: Combines conceptual understanding (Problems 1-2) with hands-on coding (Problem 3)
- **Appropriate difficulty**: The simulation study in Problem 3 is challenging but achievable with proper scaffolding
- **Proper use of solution markers**: All markdown and code solutions use the correct BEGIN/END SOLUTION format
- **Test cells follow conventions**: Tests have proper structure with visible and hidden sections
- **Real insight generation**: The simulation genuinely illustrates the bias-variance tradeoff with a concrete example where OLS is clearly biased

### Recommendations

1. **Fix the visible test in Problem 3e** that gives away the answer (0.4-0.6 range). This is the most impactful fix for maintaining assignment integrity.

2. **Add scaffolding to Problem 3c** by providing a hint about how `np.random.uniform` handles array bounds, or provide a partial code template. This is a common stumbling point.

3. **Add documentation links** to sklearn LinearRegression and relevant textbook sections on K-NN and bias-variance tradeoff (e.g., ISL Chapter 2.2).
---
