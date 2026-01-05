---
## Critique: DATASCI 503, Homework 7: Ensemble Methods and Decision Trees

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Problem 3 contains embedded images that may not be accessible**
   - **Location**: Cell 5 (Problem 3: Classification Tree Sketches)
   - **Description**: The problem references `attachment:Picture_A.jpg` and `attachment:Picture_B.jpg` which are embedded attachments. These images may not render properly in all environments (e.g., when the notebook is viewed on GitHub, exported, or if attachments are stripped).
   - **Why problematic**: Students may not be able to see the images, rendering the problem unsolvable. Additionally, the problem asks students to analyze "sketches" but provides no specific questions or tasks.
   - **Suggested fix**: Either (a) place images in a `data/` or `images/` folder and reference them with relative paths, or (b) provide a detailed textual description of what the images show. Also, add specific questions for students to answer about the sketches (e.g., "Describe the decision boundaries", "How many terminal nodes are shown?").

2. **Problem 3 solution is inadequate and non-verifiable**
   - **Location**: Cell 6 (Problem 3 solution)
   - **Description**: The solution merely states "The sketches above illustrate the partitioning of feature space by decision trees" without providing any substantive analysis.
   - **Why problematic**: Without visible images and without specific questions, there is no way to evaluate student responses. This is essentially an ungraded or un-gradable problem.
   - **Suggested fix**: Either remove this problem entirely, replace it with a code-based visualization task, or provide specific questions with detailed expected answers.

### Moderate Issues

1. **Missing data file reference and validation**
   - **Location**: Cell 10 (Problem 4)
   - **Description**: The code assumes `data/crabs.csv` exists but there is no verification or helpful error message if the file is missing.
   - **Suggestion**: Add a check for file existence with a helpful error message, or include information in the problem statement about where to obtain the dataset.

2. **Problem 5 refits the tree unnecessarily**
   - **Location**: Cell 15
   - **Description**: After GridSearchCV already fits the best estimator, the code calls `tree_clf.fit(X_train, y_train)` again, which is redundant.
   - **Suggestion**: Remove the redundant fit call since `grid.best_estimator_` is already fitted.

3. **Inconsistent random_state usage**
   - **Location**: Cells 13, 18, 22, 25
   - **Description**: DecisionTreeClassifier in GridSearchCV has no random_state, but RandomForestClassifier and HistGradientBoostingClassifier use `random_state=42`. This inconsistency could lead to different results across runs for the decision tree.
   - **Suggestion**: Add `random_state=42` to the DecisionTreeClassifier for reproducibility.

4. **Problem 7 hint references deprecated method**
   - **Location**: Cell 21 (Problem 7)
   - **Description**: The hint suggests using `staged_predict`, but `HistGradientBoostingClassifier` in newer scikit-learn versions may have different behavior or the method might work differently than expected.
   - **Suggestion**: Verify the API still works as described and add a note about which scikit-learn version is required.

5. **Test cells missing hidden test coverage for Problem 5 parts (b) and (c)**
   - **Location**: Cell 14
   - **Description**: Problem 5 asks students to (a) find optimal max_leaf_nodes, (b) plot and comment on variables, and (c) compute errors. The test cell only validates part (a). Parts (b) and (c) have no automated testing.
   - **Suggestion**: Add assertions for the existence of error calculations or move the plotting/analysis code to a solution cell with a separate markdown response cell.

6. **Variable importance comparison answer is vague**
   - **Location**: Cell 20 (Problem 6 solution)
   - **Description**: The solution says "FL... may be further down the list" which is imprecise. Solutions should provide concrete expected observations.
   - **Suggestion**: Provide more specific expected results or note that results may vary, and explain what patterns students should look for regardless of exact ordering.

### Minor Issues

- **Problem header inconsistency**: Problem 3 uses "Classification Tree Sketches" without following the "Problem N: Title" format consistently with an actual task description.
- **Warning suppression**: Cell 8 uses `warnings.filterwarnings("ignore")` which hides potentially useful diagnostic information. Consider suppressing only specific warnings.
- **Hardcoded optimal M value**: In cell 25, `optimal_m = 40` is hardcoded. Students should be required to determine this value themselves and store it.
- **Missing test for Problem 8**: There are no test assertions for the final comparison problem, though this is acceptable for a free-response question.
- **Inconsistent error rounding**: Some error outputs use `round()` and others don't, leading to inconsistent decimal places in displayed results.

### Strengths

1. **Clear progression**: The assignment builds logically from conceptual questions (Problems 1-3) to applied problems (Problems 4-8), providing good scaffolding.
2. **Comprehensive coverage**: The assignment covers decision trees, random forests, and gradient boosting, giving students exposure to multiple ensemble methods.
3. **Practical dataset**: Using the crabs dataset provides a real-world classification context with meaningful features.
4. **Good mix of theory and practice**: Problems 1 and 2 test conceptual understanding while later problems require implementation.
5. **Proper use of solution markers**: All solutions correctly use the `> BEGIN SOLUTION` / `> END SOLUTION` format for free-response and `# BEGIN SOLUTION` / `# END SOLUTION` for code.
6. **Multi-part problems with clear structure**: Problems 5-7 have clear sub-parts (a), (b), (c) that guide student work.
7. **Visualization requirements**: Requiring plots (tree visualization, importance plot, error curves) reinforces good data science practice.

### Recommendations

1. **Fix or remove Problem 3**: This problem is currently unusable due to potentially inaccessible images and lack of specific questions. Either provide accessible images with concrete questions or replace with a code-based visualization exercise.

2. **Add random_state to DecisionTreeClassifier**: Ensure reproducibility across all models by adding `random_state=42` to the GridSearchCV estimator in Problem 5.

3. **Improve test coverage for multi-part problems**: Add assertions or validation for all graded components of Problems 5-7, particularly for the analysis/commentary portions. Consider requiring students to store computed error values in named variables that can be tested.

---
