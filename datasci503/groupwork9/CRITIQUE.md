---
## Critique: DATASCI 503, Group Work 9: PCA and Clustering

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

1. **Notebook Contains Execution Errors in Review Section**
   - **Location**: Cells 5-25 (crabs.csv examples)
   - **Description**: The notebook cells showing crabs dataset examples all have `NameError` outputs because the notebook was not executed in order before saving. The PCA object also shows `AttributeError` for attributes like `n_components_` because `pca.fit(X)` never ran successfully.
   - **Why problematic**: Students will see confusing error outputs in the instructional section, undermining confidence in the material. The review section should demonstrate working code, not broken examples.
   - **Suggested fix**: Re-execute the notebook from scratch before distribution, or clear all outputs and ensure the crabs.csv file is present in the working directory.

2. **Missing Data File: crabs.csv**
   - **Location**: Cell 5
   - **Description**: The code references `crabs.csv` but this file may not exist in the assignment directory, causing all subsequent cells to fail.
   - **Why problematic**: Students cannot run the review section examples, which defeats the purpose of having worked examples before the problems.
   - **Suggested fix**: Either include the crabs.csv file in the assignment directory, use a dataset available from a library (like seaborn's built-in datasets), or download it programmatically.

### Moderate Issues

1. **Problem 5: Variable Naming Inconsistency**
   - **Location**: Cell 53-54
   - **Description**: The problem asks students to create `X = ZL + epsilon`, but the solution uses different variable names (`latent_samples`, `projection_matrix`, `data_matrix`). The test cell then references these solution-specific variable names, which students wouldn't know to use.
   - **Suggestion**: Either specify the exact variable names students should use in the problem statement, or use the mathematical notation (`Z`, `L`, `X`) consistently.

2. **Problem 7: Unclear Variable Requirements**
   - **Location**: Cells 59-61
   - **Description**: The test cell checks for `pca_model` and `explained_variance_cumsum`, but these variable names are not specified in the problem. Students may use different names and fail the tests.
   - **Suggestion**: Explicitly state: "Store your PCA model in `pca_model` and the cumulative variance in `explained_variance_cumsum`."

3. **Problem 8a: Redundant PCA Fitting Inside Loop**
   - **Location**: Cell 65
   - **Description**: The solution creates a new PCA object and fits it inside each loop iteration, which is inefficient. The PCA transformation should be done once outside the loop.
   - **Suggestion**: Fix the solution to fit PCA once, then reuse the transformed data for all clustering runs.

4. **Inconsistent Hidden Test Assertions**
   - **Location**: Problem 3 (Cell 48), Problem 12 (Cell 91)
   - **Description**: Some hidden tests make assumptions that may not hold (e.g., "Best clustering should likely use PCA-transformed data" in Problem 12). If the data or random seeds change, these could fail for correct implementations.
   - **Suggestion**: Replace assumption-based hidden tests with implementation checks that verify correctness without assuming specific outcomes.

5. **Problem 6 and 8a: Identical Structure**
   - **Location**: Cells 55-56 and 64-66
   - **Description**: Problems 6 and 8a are essentially the same task (create 2x3 subplot grid with K-means clustering), just on different data. This feels repetitive.
   - **Suggestion**: Consider combining these into one problem with sub-parts, or differentiate them more clearly by asking for additional analysis.

6. **Missing Documentation Links**
   - **Location**: Throughout
   - **Description**: While scanpy and scikit-learn are used extensively, there are no direct links to documentation for functions like `KMeans`, `AgglomerativeClustering`, or `adjusted_rand_score`.
   - **Suggestion**: Add documentation links in the problem descriptions, especially for unfamiliar libraries like scanpy.

### Minor Issues

- **Cell 3**: `warnings.filterwarnings("ignore")` suppresses all warnings, which is bad practice for learning. Consider suppressing only specific warnings if needed.

- **Cell 28**: The plotly dendrogram example uses `X` as a variable name, which shadows the pandas usage later. Consider using a different name like `X_demo_dendrogram`.

- **Problem 1**: The docstrings use `data` as the parameter name, but the function calls use `X_demo`. This is fine but slightly inconsistent with the problem description.

- **Problem 2**: The hint mentions `sklearn.metrics.pairwise_distances` but doesn't explain what it returns (distance matrix dimensions, etc.).

- **Problem 4**: Free response format has extra newline before `> END SOLUTION` compared to other free response cells.

- **Problem 9**: The phrase "write the number of observations and the number of features in each dataset in the assert statement block" is confusing. It should say "fill in the correct values for the variables."

- **Cell 51**: Transition text "We have demonstrated how PCA works..." appears between Problem 4 and Problem 5, breaking the flow of the problems section.

- **Problem 11a**: Uses `metric="euclidean"` parameter which is the default; could be simplified or explained why it's explicit.

### Strengths

1. **Excellent Theoretical Foundation**: The review section provides a comprehensive mathematical treatment of PCA with clear notation and formulas for eigendecomposition, loadings, and variance explained.

2. **Well-Structured Progression**: The assignment builds logically from implementing basic metrics (TSS/WSS/BSS) to implementing K-means from scratch to applying these concepts to real gene expression data.

3. **Strong Visualizations**: The BSS/WSS visualization grid (Cell 38) is an excellent pedagogical tool that helps students intuitively understand what good clustering looks like.

4. **Real-World Application**: Using the PBMC gene expression dataset gives students exposure to actual single-cell data analysis workflows, which is highly relevant for data science.

5. **Good Balance of Theory and Practice**: Problems range from implementing algorithms (Problems 1-3), to interpretation (Problems 4, 8b), to application (Problems 10-12).

6. **Proper Test Structure**: Test cells follow the required format with visible assertions, error messages, and hidden tests for autograding.

7. **Clear Free Response Markers**: Free response problems correctly use blockquote-style markers.

### Recommendations

1. **Fix the crabs dataset issue**: Either include the CSV file, switch to a built-in dataset (e.g., `sns.load_dataset("iris")`), or download it from a reliable URL. Re-execute the notebook to clear all errors.

2. **Standardize variable naming in problems**: For each problem, explicitly state what variable names students should use so tests pass reliably. Consider using a consistent pattern like providing starter variable assignments.

3. **Add documentation links**: For each new function or library introduced (especially scanpy), add a hyperlink to the official documentation in the problem description or a preceding markdown cell.
---
