---
## Critique: DATASCI 503, Homework 8: Support Vector Machines

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Missing Data File and No Instructions for Obtaining It**
   - **Location**: Problem 4, cell-10
   - **Description**: The code references `data/crabs.csv` but there are no instructions for students on where to obtain this data file or how to load it.
   - **Why Problematic**: Students cannot complete Problem 4 without the data file. This will cause immediate errors and confusion.
   - **Suggested Fix**: Either include the data file in the assignment directory, provide a download link (e.g., from the MASS R package documentation), or add code to load it from a URL. Add a markdown cell explaining where the data comes from and what it contains.

2. **Problem 4 Parts Lack Clear Deliverables and Analysis Questions**
   - **Location**: Problem 4 (a), (b), (c)
   - **Description**: Each part asks students to "plot" and test various hyperparameters but never asks them to interpret results, compare kernel performance, or draw conclusions about which model is best for this data.
   - **Why Problematic**: The problem becomes a mechanical exercise in running code rather than developing understanding. Students should be asked to analyze the plots, explain why certain C values or kernels perform better, and make a final recommendation.
   - **Suggested Fix**: Add parts (d) and (e) asking students to: (d) Compare the best-performing models from each kernel type and explain which performs best and why; (e) Evaluate the final chosen model on the held-out test set and report test error.

### Moderate Issues

1. **No Explanation of the C Hyperparameter**
   - **Location**: Problem 4 introduction
   - **Description**: The assignment introduction mentions slack variables but Problem 4 jumps directly to tuning C without explaining what C controls or how it relates to the soft-margin SVM concepts from Problems 2-3.
   - **Suggestion**: Add a brief explanation that C controls the trade-off between maximizing margin and minimizing slack variable violations. Link this to the slack variable concepts in Problem 3.

2. **Inconsistent Problem Header Format**
   - **Location**: Problem 4 subparts
   - **Description**: Problem 4 uses `#### Part (a): Linear SVM` headers which differs from the `### Problem N: Title` format used for main problems. The CLAUDE.md specifies `### Problem N: Title` format.
   - **Suggestion**: Use `#### Problem 4a: Linear SVM` or keep the current subpart format but ensure consistency with the style guide.

3. **Test Cells Have Hardcoded Magic Numbers**
   - **Location**: cell-14, cell-18, cell-22
   - **Description**: Hidden tests contain magic numbers like `200` (number of C values) and `0.15` (expected minimum error) that depend on specific solution implementation choices.
   - **Suggestion**: Make tests more robust by checking relative properties (e.g., `len(c_values) > 50`) rather than exact values, or document the expected solution approach more clearly.

4. **Missing Documentation Links**
   - **Location**: Problem 4 hint
   - **Description**: The hint mentions `sklearn.svm.SVC` and `StandardScaler` but provides no links to documentation.
   - **Suggestion**: Add links to scikit-learn documentation: `sklearn.svm.SVC`, `StandardScaler`, and `cross_val_score`.

5. **No Guidance on C Value Range Selection**
   - **Location**: Problem 4
   - **Description**: Students are told to test "a range of values of the C hyperparameter" but given no guidance on what range is reasonable or how to choose it. The solution uses `np.arange(0.01, 2.01, 0.01)` but this is somewhat arbitrary.
   - **Suggestion**: Either provide the C range to use, or add guidance on how to select hyperparameter ranges (e.g., logarithmic spacing, starting wide then narrowing).

6. **Gamma Values in Part (c) Should Use Logarithmic Scale**
   - **Location**: Problem 4(c)
   - **Description**: The solution tests `gamma_values = [0.01, 0.1, 1, 5, 10]` but the problem only says "at least three values of gamma" without guidance. Gamma is typically varied on a log scale.
   - **Suggestion**: Recommend using logarithmic spacing (e.g., `np.logspace(-3, 2, 6)`) and explain why log-scale is appropriate for kernel hyperparameters.

### Minor Issues

- **Problem 1 title includes "(ISLP 9.2)"** - While helpful as a reference, this may confuse students who don't have access to the ISLP textbook. Consider moving the reference to a note.
- **Problem 2 reference to "equation (9.1) in ISLP"** - Same issue; students need access to the textbook to understand this reference.
- **Inconsistent use of $m$ vs margin** - Problem 3(b) defines margin as $m = \sqrt{2}$ but the concept of margin width vs. margin lines could be clearer.
- **No seed set for KFold in problem instructions** - While the solution uses `random_state=42`, students might get different results without this guidance.
- **Solution code uses `visible=True` in `plt.grid()`** - This is redundant since `True` is the default; minor style issue.

### Strengths

1. **Good progression of difficulty**: The assignment moves logically from conceptual understanding (Problems 1-2), to mathematical derivation (Problem 3), to practical implementation (Problem 4).

2. **Strong theoretical foundation**: Problems 1-3 from ISLP provide excellent coverage of the geometry and mathematics of SVMs before students implement them.

3. **Appropriate use of cross-validation**: Problem 4 correctly emphasizes the importance of cross-validation for hyperparameter tuning.

4. **Good use of pipelines**: The solution demonstrates proper use of sklearn Pipelines to ensure scaling is applied correctly within cross-validation.

5. **Clear solution explanations**: The free-response solutions are thorough and well-organized with clear mathematical notation.

6. **Comprehensive kernel coverage**: Problem 4 covers linear, polynomial, and RBF kernels, giving students exposure to the main SVM kernel types.

### Recommendations

1. **Priority 1**: Add the crabs dataset to the assignment directory and include a brief description of the data (source, variables, sample size). This is blocking for students.

2. **Priority 2**: Add analysis/interpretation questions to Problem 4 asking students to compare kernels, explain results, and evaluate on the test set. This transforms a coding exercise into a learning experience.

3. **Priority 3**: Add documentation links to sklearn classes and provide clearer guidance on hyperparameter range selection, especially recommending log-scale for gamma and possibly C.

---
