---
## Critique: DATASCI 503, Group Work 6: Splines and GAMs

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

1. **Deprecated Pandas API Warning**
   - **Location**: Cell 27 (loading auto-mpg dataset)
   - **Description**: The code uses `pd.read_csv(..., delim_whitespace=True, ...)` which is deprecated. The `delim_whitespace` parameter has been deprecated in favor of `sep='\s+'`.
   - **Why problematic**: Students running this code will receive deprecation warnings, which can be confusing and suggests the course materials are not maintained.
   - **Suggested fix**: Replace `delim_whitespace=True` with `sep=r'\s+'` or `sep='\\s+'`.

2. **Hidden Test Uses Hardcoded Random Values Without Verification Path**
   - **Location**: Cell 46 (Problem 1 hidden tests)
   - **Description**: The hidden test asserts `expected_sum = np.array([204, 129, 76, 170, 123, 270, 28])` which depends on the specific random seed. If students correctly implement the function but use a slightly different interpretation of boundary conditions, they have no way to debug.
   - **Why problematic**: The visible tests only check structural properties (sum equals n_samples, row sums equal 1), not actual correctness of bin assignment. A student could pass all visible tests with an off-by-one error at boundaries.
   - **Suggested fix**: Add a visible test that checks the simple example from the problem statement:
     ```python
     X_simple = np.array([1, 2, 4, 6, 7, 9])
     knots_simple = np.array([3, 6])
     design_simple = piecewise_constant_design_matrix(X_simple, knots_simple)
     expected = np.array([[1,0,0], [1,0,0], [0,1,0], [0,0,1], [0,0,1], [0,0,1]])
     assert np.array_equal(design_simple, expected), "Simple example should match expected"
     ```

### Moderate Issues

1. **Missing Link for NHANES Data Files**
   - **Location**: Problem 3 (Cell 52-54)
   - **Description**: The problem references local files (`data/BMX_L.xpt`, `data/DEMO_L.xpt`, `data/HDL_L.xpt`) but does not explain where students should download them from.
   - **Suggestion**: Add instructions for downloading the data files from the CDC NHANES website or provide a setup cell that downloads them automatically.

2. **Inconsistent Input Shape Handling**
   - **Location**: Problem 1 solution (Cell 45)
   - **Description**: The function docstring says `X` is a "1D array" but the solution immediately reshapes it: `X = X.reshape(-1, 1)`. The test also passes `X = x.reshape(-1, 1)` (already 2D). This inconsistency could confuse students.
   - **Suggestion**: Clarify in the docstring whether X should be 1D or 2D, and ensure tests match the documented interface.

3. **"Think About" Questions Have No Expected Engagement**
   - **Location**: Cells 18, 24, 32
   - **Description**: Three "Think About" questions are posed but there's no indication whether students should answer them, discuss with partners, or if they're rhetorical. The one about integral limits (Cell 18) is never answered anywhere.
   - **Suggestion**: Either convert these to graded free-response problems or add brief inline answers for self-study.

4. **Problem 3 Lacks Intermediate Verification**
   - **Location**: Cell 53-54
   - **Description**: Students must figure out variable names from external documentation, merge three datasets, rename columns, and drop NAs. If anything goes wrong, the only visible test is the final shape check.
   - **Suggestion**: Add intermediate assertions or print statements showing expected shapes after each merge, or provide the column mapping in the problem statement.

5. **Problem 5 GridSearchCV Hidden Test Has Wrong Expected Shape**
   - **Location**: Cell 62 hidden tests
   - **Description**: The assertion `n_spline_features = n_features * (4 + 2 - 1)  # n_knots=4, degree=2` calculates 40 features, but SplineTransformer with n_knots=4 and degree=2 produces `n_knots + degree - 1 = 5` splines per feature, giving 40 total. However, the assertion checks for shape `(n_spline_features,)` which is a 1D tuple, while the actual shape would be `(40,)`. This seems correct but the comment formula is confusing.
   - **Suggestion**: Clarify the formula in the comment or use the actual sklearn formula for number of spline features.

6. **Problem 6 Missing Import in Student Version**
   - **Location**: Cell 65
   - **Description**: The solution imports `train_test_split` inside the solution block. Students would not have this import available in the student version.
   - **Suggestion**: Move the import to the requirements cell at the top of the notebook, or add it above the `# BEGIN SOLUTION` marker.

### Minor Issues

1. **Grammar**: Cell 18 - "the limits of the integral defining the objective?" - should clarify these are the integration bounds (min and max of x).

2. **Redundant reshape**: Cell 44 example shows `X` as a column vector but the mathematical notation shows it as a simple vector. The visual distinction could be clearer.

3. **Missing error messages in some assertions**: Cell 46 has assertions without error messages (e.g., `assert np.all(X_design.sum(axis=1) == 1)` should have a descriptive message).

4. **Cell 41 hardcoded y-limits**: The `ax.set_ylim(-30, 30)` may clip partial dependence plots for different datasets or random seeds.

5. **Cell 27 inplace modification warning**: Using `df.dropna(inplace=True)` is considered less idiomatic than `df = df.dropna()` in modern pandas.

6. **Problem 4 uses double brackets for y**: `y = my_df[['HDL']]` creates a DataFrame, but later the residual plot expects consistent types. Using `y = my_df['HDL']` (Series) would be more consistent.

7. **Missing seed in Problem 7**: The gridsearch in Problem 7 doesn't set a random state, which could lead to non-reproducible results.

8. **Cell 37 URL may become stale**: The UCI ML Repository URL for breast cancer data could change; consider using sklearn's `load_breast_cancer()` instead.

### Strengths

1. **Excellent progression**: The notebook builds logically from polynomial regression through splines to GAMs, with clear conceptual explanations at each step.

2. **Good use of visualizations**: Multiple plots help students understand how different parameters (lambda, degree, knots) affect model behavior.

3. **Real-world datasets**: Using NHANES and UCI datasets provides practical context beyond toy examples.

4. **Comprehensive coverage**: The assignment covers both regression and classification GAMs, and includes model selection via GridSearchCV.

5. **Well-structured problem headers**: Problems follow the `### Problem N: Title` format consistently.

6. **Good solution markers**: All problems properly use `# BEGIN SOLUTION` / `# END SOLUTION` markers.

7. **Hidden tests present**: All coding problems include hidden tests for robust autograding.

8. **Documentation links provided**: Links to sklearn and pygam documentation are included where relevant.

### Recommendations

1. **Priority 1**: Fix the deprecated `delim_whitespace` API and add visible tests for Problem 1 that verify the simple example from the problem statement. This will help students debug boundary condition issues.

2. **Priority 2**: Add data download instructions for Problem 3 and move the `train_test_split` import outside the solution block in Problem 6. These prevent students from being blocked on setup issues.

3. **Priority 3**: Convert at least one "Think About" question into a graded free-response problem, or provide inline answers. This ensures students engage with the conceptual material about bias-variance tradeoffs in spline fitting.
---
