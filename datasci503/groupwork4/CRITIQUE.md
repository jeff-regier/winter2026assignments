---
## Critique: DATASCI 503, Group Work 4: Linear and Quadratic Discriminant Analysis

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

1. **Missing Data Path Configuration for Problem 10**
   - **Location**: Cell 43 (Problem 10: QDA on NHANES Dataset)
   - **Description**: The solution hardcodes `data_path = "../datasets/NHANES/"` but students receive no guidance on where data should be located or how to access it. The problem statement provides no starter code or data loading instructions.
   - **Why problematic**: Students will encounter `FileNotFoundError` and not know how to proceed. This is a complete blocker for completing the problem.
   - **Suggested fix**: Add starter code that loads the data for students, or provide clear instructions with the data path. Consider including a data loading cell before the problem that students can reference, similar to how the breast cancer dataset is loaded in Problem 8.

2. **Problem 10-11 Structure Violates Cell Separation Rule**
   - **Location**: Cells 43-46 (Problems 10 and 11)
   - **Description**: Problems 10 and 11 have their entire solutions in single cells, including data loading, preprocessing, model fitting, and visualization. The test cells reference variables created in the solution cells without any starter code structure.
   - **Why problematic**: The test cells depend on variables (`qda`, `y_pred`, `y_test`, `X_scaled`, `X_train`, `X_test`, `xx`, `yy`, `Z`) that students must create with exact names. Students have no guidance on expected variable names or code structure.
   - **Suggested fix**: Provide starter code skeleton with variable names and structure. Break down into smaller, testable components. For example:
     ```python
     # Load and preprocess data (provided)
     # ... data loading code ...

     # TODO: Create HDL_group column using thresholds
     my_df["HDL_group"] = ...  # SOLUTION

     # TODO: Scale features and split data
     X_scaled = ...  # SOLUTION
     X_train, X_test, y_train, y_test = ...  # SOLUTION
     ```

### Moderate Issues

1. **Inconsistent Problem Header Format**
   - **Location**: Multiple cells (e.g., cells 14-16, 42-43)
   - **Description**: Most problems use `### Problem N: Title` but some markdown header formatting is inconsistent. Problem 10 uses proper format but the problem statement lacks structure compared to earlier problems.
   - **Suggestion**: Ensure all problems follow the exact format `### Problem N: Title` with clear requirements listed.

2. **Missing Hints for np.einsum Problems**
   - **Location**: Cells 22-27 (Problems 4 and 5)
   - **Description**: The problems mention using `np.einsum` as a hint but provide no guidance on einsum notation or examples. Students unfamiliar with einsum will struggle significantly.
   - **Suggestion**: Add a brief example of einsum usage, or link to NumPy einsum documentation. For example: "The einsum notation `np.einsum('ij,jk->ik', A, B)` computes matrix multiplication. See [NumPy einsum documentation](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html)."

3. **Weak Visible Tests Give Away Solution Structure**
   - **Location**: Cell 18 (Problem 2 tests)
   - **Description**: Test case 2 uses `expected4 = 2` which is a suspiciously round number that could be reverse-engineered. The test essentially reveals that with identity covariance, zero prior log, and mu=[2,2], the answer is simply x.dot(mu) - 0.5*mu.dot(mu) = 6 - 4 = 2.
   - **Suggestion**: Use less obvious expected values or add more test cases with non-trivial covariances in visible tests.

4. **Free Response Problems Lack Rubric Guidance**
   - **Location**: Cells 14-15 (Problem 1), 29-30 (Problem 6), 40-41 (Problem 9)
   - **Description**: Free response problems ask for definitions and parameter counts but provide no guidance on expected depth or format of answers.
   - **Suggestion**: Add expectations like "Your answer should include the mathematical formula and a brief explanation of each term" or "Express your answer as a formula in terms of k and d."

5. **Problem 10 Missing Clear Requirements**
   - **Location**: Cell 42
   - **Description**: The problem statement mentions to "scale your data and split it into train and test sets" but does not specify the test size, random state, or whether to print accuracy.
   - **Suggestion**: Add specific requirements: "Use a test size of 0.2 and random_state=42 for reproducibility. Report the test accuracy."

6. **No Error Messages in Some Hidden Tests**
   - **Location**: Cells 44, 47
   - **Description**: Some hidden tests use generic assertions without descriptive error messages.
   - **Suggestion**: Add descriptive messages like `assert len(X_train) > len(X_test), "Training set should be larger than test set"`.

### Minor Issues

- **Cell 1**: Imports `make_blobs` from sklearn but it's only used in instructor examples, not student code. Consider consolidating imports.

- **Cell 4**: Uses hardcoded random seed `np.random.seed(42)` in example code. While fine for reproducibility, a comment explaining why would be helpful.

- **Cell 17**: The docstring says "Returns: float" but could return a numpy scalar depending on input shapes. Consider specifying `float | np.floating`.

- **Cell 24**: The helper function `predict_vectorized_single` is defined between the solution cell and test cell. This should be in the test cell for clarity.

- **Cell 28**: Defines `predict_vectorized` helper inside the test cell - this is good, but the function is never used after the tests.

- **Cell 36**: Uses `from sklearn.model_selection import train_test_split` and `from sklearn.preprocessing import StandardScaler` inside the test cell, but these are already imported in cell 1.

- **Cell 43**: Uses seaborn for heatmap but seaborn is not imported at the top of the notebook.

- **Problem 11**: The test assertions are minimal - only checking shapes and valid class labels. Could test that the decision boundary shows non-trivial regions.

### Strengths

1. **Excellent theoretical foundation**: The notebook provides clear mathematical derivations for both LDA and QDA, connecting the Bayes classifier theory to practical implementation.

2. **Strong progressive scaffolding**: Problems build naturally from implementing single functions to vectorized versions to full class implementations.

3. **Good use of visualizations**: The notebook includes helpful plots showing class distributions, decision boundaries, and the Bayes error rate concept.

4. **Real-world dataset application**: Problem 10 uses NHANES health data, which is relevant and engaging for data science students.

5. **Thorough hidden tests**: Most problems have comprehensive hidden tests that check edge cases, shapes, and correctness beyond visible tests.

6. **Clear code structure**: The instructor solutions demonstrate clean, idiomatic NumPy code with proper type hints and docstrings.

### Recommendations

1. **[CRITICAL] Add data loading starter code for Problem 10**: Provide the NHANES data loading code as starter code, not as part of the solution. Students should focus on the QDA implementation, not debugging file paths.

2. **[CRITICAL] Restructure Problems 10-11 with starter code**: Break these problems into smaller testable units with explicit variable names in starter code. This matches the structure of earlier problems and makes grading more reliable.

3. **[MODERATE] Add np.einsum tutorial or examples**: Before Problems 4 and 5, add a brief explanation of einsum notation with a worked example, or link to documentation. This is a powerful but often unfamiliar tool for students.
---
