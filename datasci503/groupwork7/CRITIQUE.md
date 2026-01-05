---
## Critique: DATASCI 503, Group Work 7: Trees and Tree Ensembles

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

1. **Missing Data Files for Problem 2**
   - **Location**: Problem 2 (cell-56, cell-57)
   - **Description**: The problem asks students to load NHANES data files (`BMX_L.xpt`, `DEMO_L.xpt`, `HDL_L.xpt`) from a `data/` directory, but there is no indication that these files are provided or instructions on how to obtain them.
   - **Why problematic**: Students cannot complete Problems 2-10 without access to these data files. The assignment provides a download mechanism for the spambase dataset but not for the NHANES dataset.
   - **Suggested fix**: Either (a) add code to download the NHANES .xpt files similar to the spambase download, (b) provide explicit instructions for students to download the files manually with URLs, or (c) ensure the data files are included in the assignment distribution.

2. **Problem 6 Visible Test Cases May Fail Due to Data Variability**
   - **Location**: Problem 6 test cell (cell-70)
   - **Description**: The visible tests check specific row indices (`my_df.iloc[6]`, `my_df.iloc[155]`, `my_df.iloc[20]`) for expected Level values. However, after dropping NaN values, the row indices may shift unpredictably depending on which rows had missing values.
   - **Why problematic**: Students with correct implementations may fail these tests if the DataFrame indices don't align with the expected values after `dropna()`. This creates confusion and wastes debugging time.
   - **Suggested fix**: Reset the index after `dropna()` in Problem 2 requirements, or use more robust tests that don't depend on specific row positions (e.g., check that a sample of rows with known HDL/Gender values produce correct Level classifications).

### Moderate Issues

1. **Inconsistent Variable Naming in Problem 4 Print Statement**
   - **Location**: Problem 4 solution cell (cell-63)
   - **Description**: The print statement for Boosting is split across two lines awkwardly: `print(f"Boosting - Train: {train_mse_boosting:.2f}, Val: {validation_mse_boosting:.2f}")` followed by `print(f"         Test: {test_mse_boosting:.2f}")`.
   - **Suggestion**: Either keep all metrics on one line or use consistent formatting across all three models.

2. **Missing Documentation Links in Problem 2**
   - **Location**: Problem 2 (cell-56)
   - **Description**: The problem provides links to NHANES documentation pages, but these are for viewing variable descriptions, not for downloading data. Students need clearer guidance on obtaining the actual .xpt files.
   - **Suggestion**: Provide direct download links to the .xpt files or add code to fetch them programmatically.

3. **Problem 10 Accuracy Threshold May Be Arbitrary**
   - **Location**: Problem 10 (cell-82, cell-84)
   - **Description**: The 57% accuracy threshold seems somewhat arbitrary. Without context about baseline performance or class distribution, students may not understand what constitutes good performance.
   - **Suggestion**: Add context about the baseline accuracy (e.g., majority class predictor) and explain why 57% represents meaningful improvement.

4. **Problem 9b Expected Answer Depends on Random Results**
   - **Location**: Problem 9b (cell-81)
   - **Description**: The solution notes "The exact ranking may vary depending on the random state and data split," but the problem doesn't acknowledge this variability to students.
   - **Suggestion**: Either explain to students that rankings may vary, or structure the question to focus on methodology rather than a specific ranking.

5. **Weak Visible Tests in Problem 4**
   - **Location**: Problem 4 test cell (cell-64)
   - **Description**: The visible tests only check that MSE values are non-negative, which provides minimal validation. A student could return any positive number and pass.
   - **Suggestion**: Add more informative visible tests, such as checking that MSE values are within reasonable ranges (e.g., < 1000) or that training MSE is less than a random baseline.

6. **Problem 7 Print Statement Formatting Inconsistency**
   - **Location**: Problem 7 solution cell (cell-72)
   - **Description**: Same awkward line-break issue as Problem 4 for the Boosting output.
   - **Suggestion**: Use consistent formatting across all print statements.

### Minor Issues

- **Typo in cell-2**: "Gini impurity, entropy for classification, and mean squared error, mean absolute error for regression" - could use parallel structure ("and" before last item in each list).
- **Missing period** at end of Problem 1 prompt.
- **Inconsistent use of code formatting**: Some variable names in markdown are formatted with backticks (e.g., `my_df`) while others are not.
- **Problem 2 says "You may need to refer to the documentation"** but the documentation links point to HTML pages, not the actual variable mappings students need.
- **Cell-4**: The link text says "this [link]" - consider making the link text more descriptive (e.g., "the UCI Machine Learning Repository").
- **Problem 6 HDL thresholds**: The Cleveland Clinic thresholds may differ from other sources. Consider citing the specific source or noting that thresholds can vary.
- **Section header formatting inconsistency**: "## Classification Trees" and "## Comparing different splitting criterions" use different capitalization styles (title case vs. sentence case).
- **"criterions" in cell-23**: Should be "criteria" (plural of criterion).

### Strengths

1. **Excellent expository content**: The assignment provides clear explanations of decision trees, random forests, and boosting with appropriate mathematical notation and conceptual framing.

2. **Good progression of difficulty**: Problems build naturally from data preparation (Problem 2) through model training (Problems 4, 7) to analysis and optimization (Problems 9, 10).

3. **Real-world dataset application**: Using NHANES health data makes the classification problem meaningful and helps students understand practical implications of model errors.

4. **Thoughtful free-response questions**: Problems 1, 9a, and 9b encourage critical thinking about when to use tree methods and the real-world costs of misclassification.

5. **Comprehensive coverage**: The assignment covers both regression and classification trees, multiple ensemble methods, feature importance (both impurity-based and permutation), and hyperparameter tuning.

6. **Good use of visualizations**: Confusion matrices, feature importance plots, and decision tree visualizations help students understand model behavior.

7. **Appropriate scaffolding**: The introductory walkthrough with the spam dataset provides a worked example before students tackle the NHANES problems independently.

### Recommendations

1. **Add NHANES data download code** (Critical): Include programmatic download of the NHANES .xpt files similar to how spambase is fetched, ensuring students can complete the assignment without manual file management.

2. **Fix row-index-dependent tests** (Critical): Rewrite Problem 6 tests to not depend on specific DataFrame indices, or require students to reset indices after `dropna()` in Problem 2.

3. **Improve visible test informativeness** (Moderate): Strengthen visible tests in Problems 4 and 7 to provide better feedback to students while not giving away solutions. For example, verify that models produce predictions of the correct shape or that ensemble methods don't have identical results to CART.
---
