---
## Critique: DATASCI 503, Group Work 3: ROC Curves and Logistic Regression

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Potential Division by Zero Not Handled in Problem 10**
   - **Location**: Cell 53 (Problem 10: Implement ROC from Scratch)
   - **Description**: The solution handles division by zero for FPR and TPR calculations, but the visible test assertions do not check for this edge case. More critically, if students do not handle this case, their implementation will fail with certain threshold values.
   - **Why problematic**: Students may submit code that works for the given dataset but fails silently or raises exceptions in edge cases. The assignment does not warn students about this potential issue.
   - **Suggested fix**: Add a hint in the problem description warning students to handle the case where (FP + TN) = 0 or (TP + FN) = 0, which can occur at extreme thresholds.

2. **Test Cell for Problem 4 Uses Wrong Denominator**
   - **Location**: Cell 36 (Test assertions for Problem 4)
   - **Description**: The test checks `len(my_df) / len(df) > 0.7`, but `df` is the joined dataset before column selection. The problem states to check against removing "more than 30% of all rows in the dataset," which should compare against the original `my_df` size. However, the `original_size` variable is computed in the solution cell.
   - **Why problematic**: The test uses `df` which may have different size than the relevant comparison (the `my_df` before dropna). If students select different columns that reduce rows during the selection step, this test may give incorrect feedback.
   - **Suggested fix**: Change the test to use `original_size` which is defined in the solution cell, or recompute the original size in the test cell for clarity.

### Moderate Issues

1. **Problem 3 Response Variable Name Inconsistency**
   - **Location**: Cell 30 (Problem 3: Select Predictor Variables)
   - **Description**: The problem mentions "response variable (`LBDHDD` for HDL)" but the solution renames it to `HDL`. This creates confusion in later problems where the code must check for both names (`"HDL" if "HDL" in my_df.columns else "LBDHDD"`).
   - **Suggestion**: Either require a specific naming convention (e.g., always rename to `HDL`) or clarify in the problem that renaming is optional and subsequent code should handle both cases.

2. **Missing Documentation Link for read_sas**
   - **Location**: Cell 24 (Problem 1: Load the NHANES Datasets)
   - **Description**: The problem tells students to load SAS files but does not provide a hint or link to `pd.read_sas()` documentation.
   - **Suggestion**: Add a hint: "**Hint:** Use `pd.read_sas()` to load SAS .xpt files. See the [Pandas read_sas documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html)."

3. **Problem 5 Threshold Ambiguity**
   - **Location**: Cell 37 (Problem 5: Create Binary HDL Indicator)
   - **Description**: The problem states HDL of "60 mg/dL or higher" is protective, then asks for a binary indicator that is True when HDL is "**greater than** 60 mg/dL". This is inconsistent (>= vs >).
   - **Suggestion**: Clarify whether the threshold should be `>= 60` or `> 60`. The medical context suggests `>= 60` would be more appropriate.

4. **Hidden Test May Fail for Valid Alternative Implementations in Problem 3**
   - **Location**: Cell 33 (Test assertions for Problem 3)
   - **Description**: The hidden test checks for specific column names (`SEQN`, `HDL` or `LBDHDD`), but students could legitimately use different column names if they rename columns differently.
   - **Suggestion**: Make the test more flexible or explicitly state required column naming conventions in the problem.

5. **Problem 8 Hidden Test Expects Boolean but Model Returns numpy bool**
   - **Location**: Cell 48 (Test assertions for Problem 8)
   - **Description**: The hidden test `assert set(predicted_hdl_healthy).issubset({True, False})` may fail because sklearn's `predict()` on a boolean target returns numpy boolean values, not Python booleans.
   - **Suggestion**: Change the test to check for boolean dtype instead: `assert predicted_hdl_healthy.dtype == bool or predicted_hdl_healthy.dtype == np.bool_`.

6. **No Warning About NHANES Data File Dependencies**
   - **Location**: Cell 23-24 (Problem 1)
   - **Description**: The assignment assumes NHANES data files exist at `../datasets/NHANES/` but provides no fallback or error message if files are missing.
   - **Suggestion**: Add a check at the beginning of the group work section that verifies the data files exist and provides a helpful error message if they do not.

### Minor Issues

- **Cell 2**: The phrase "Let us visualize how the generated data looks like" should be "Let us visualize what the generated data looks like" or "Let us visualize how the generated data looks."
- **Cell 22**: The introductory sentence "For group work, we will attempt to use and program the ROC from scratch" is awkward. Consider: "For group work, we will implement ROC from scratch."
- **Cell 23**: The preview cell (before Problem 1) duplicates the loading that students will do in Problem 1. This is pedagogically useful for exploration but creates redundant code.
- **Cell 30**: Problem 3 part (a) asks students to write in a markdown cell, but the markdown solution cell is not clearly labeled as the place to write (students might be confused about which cell to use).
- **Cell 52**: The docstring in Problem 10 says `predicted_probs_positive` but the function is called with `predicted_probs[:, 1]` - this is technically correct but could be clarified.

### Strengths

1. **Excellent pedagogical progression**: The assignment builds from using sklearn's ROC functions to implementing ROC from scratch, helping students understand the underlying concepts rather than just using black-box functions.

2. **Good use of real-world data**: Using the NHANES dataset provides authentic data science experience with real health data, making the exercise more engaging and relevant.

3. **Comprehensive coverage of ROC concepts**: The assignment covers soft vs. hard classifiers, thresholding, confusion matrices, TPR/FPR, precision-recall curves, and ROC curves in a logical sequence.

4. **Well-structured test cells**: Most test cells follow the correct format with visible assertions and hidden tests for autograding.

5. **Helpful hints and documentation links**: Most problems include hints pointing to relevant sklearn documentation.

6. **Clear connection to medical interpretation**: Problem 5 provides real medical context for the HDL cholesterol threshold, making the binary classification task meaningful.

7. **Good visualization throughout**: The assignment includes multiple plots that help students understand the data and results visually.

### Recommendations

1. **Fix the division by zero handling in Problem 10**: Add explicit guidance about handling edge cases when computing TPR and FPR, and add visible tests that check for this.

2. **Standardize column naming**: Either require students to use specific column names after Problem 3, or refactor subsequent problems to be agnostic to naming choices. The current approach with `"HDL" if "HDL" in my_df.columns else "LBDHDD"` in solutions is fragile.

3. **Clarify the HDL threshold in Problem 5**: Resolve the inconsistency between "60 or higher" in the explanation and "> 60" in the implementation requirement. Consider using `>= 60` to match the medical guidance quoted.
---
