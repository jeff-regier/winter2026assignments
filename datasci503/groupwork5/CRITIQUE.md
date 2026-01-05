---
## Critique: DATASCI 503, Group Work 5: Cross Validation

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

#### 1. Inconsistent `weights` Parameter in KNN Problems
**Location:** Problems 8, 9, and 10 (cells 70, 73, 77)

**Description:** The solution in Problem 8 uses `weights="distance"` for the KNeighborsClassifier, and the function in Problem 9 also uses `weights="distance"`. However, Problem 10's solution uses the default `weights="uniform"`. This inconsistency means the "best K" found in Problem 9 was evaluated with distance weighting, but the final model in Problem 10 is trained without it.

**Why problematic:** Students who correctly follow the pattern from Problem 9 will get different results than the provided solution. The hyperparameter tuning was done with one configuration but the final model uses a different configuration, which is methodologically incorrect.

**Suggested fix:** Either consistently use `weights="distance"` in all KNN problems, or consistently use the default. Also, the problem statements should explicitly specify whether to use distance weighting.

#### 2. Missing Data Files or File Path Specification
**Location:** Problem 1 (cell 38)

**Description:** The solution assumes data files exist at `data/BMX_L.xpt`, `data/DEMO_L.xpt`, and `data/HDL_L.xpt`, but the assignment never tells students where to find these files or confirms they exist in that location.

**Why problematic:** Students cannot complete the assignment if the data files are not present or if they don't know the correct path. The assignment mentions "Our favorite (and only) dataset" suggesting prior use, but provides no setup instructions.

**Suggested fix:** Add a data setup section that either provides download links to the NHANES data files or confirms the file paths. Consider adding assertions or helpful error messages if files are not found.

### Moderate Issues

#### 1. Problem 6a Solution Uses Manual Loop Instead of cross_val_score
**Location:** Problem 6a (cell 55)

**Description:** The solution implements manual fold iteration with `cv.split()` rather than using `cross_val_score`, even though the earlier `KFoldCV` function (Problem 4) uses `cross_val_score` and the problem says students can use sklearn utilities.

**Suggestion:** For consistency and to reinforce best practices, the solution could use `cross_val_score` with a loop over C values, similar to the pattern established in Problem 4.

#### 2. Using `.iloc` Assumes DataFrame Input in KFoldCV_L2 and KFoldCV_NN
**Location:** Problems 6a and 9 (cells 55, 73)

**Description:** The solutions use `X.iloc[train_idx]` and `y.iloc[train_idx]`, which only works for pandas DataFrames/Series. If a student passes numpy arrays (which would be reasonable given the earlier examples), this will fail.

**Suggestion:** Use bracket indexing that works for both arrays and DataFrames: `X[train_idx]` for arrays, or explicitly handle both cases.

#### 3. No Explanation of Why Use Different K Values for KNN
**Location:** Problem 9 (cell 72)

**Description:** The problem specifies exact K values [1, 3, 5, 10, 15, 20, 25, 35, 50, 100] without explaining why these specific values were chosen or why covering this range is important.

**Suggestion:** Add a brief pedagogical note about why we test multiple values and why the range matters (e.g., covering small K that may overfit to large K that may underfit).

#### 4. Stratified Splitting Mentioned But Not Used Consistently
**Location:** Problem 3 vs Problem 4

**Description:** Problem 3 correctly emphasizes using stratified sampling in train_test_split, but the KFoldCV function in Problem 4 uses regular KFold rather than StratifiedKFold. This is inconsistent.

**Suggestion:** Either use StratifiedKFold in the KFoldCV function to maintain consistency with the stratification reasoning, or explain why stratification is less critical for cross-validation folds.

#### 5. Problem 7b Question Does Not Match Context
**Location:** Problem 7b (cell 63)

**Description:** The question asks about retraining on "merged train+val dataset" but the assignment never explicitly separated a validation set from training. Cross-validation was used, which uses temporary folds, not a held-out validation set.

**Suggestion:** Reword to "Explain why we retrain the model on the full training set (all data except the test set) before final evaluation" to match what was actually done.

#### 6. Hidden Tests May Give Away Solution Details
**Location:** Problem 2 hidden tests (cell 42)

**Description:** The hidden test `assert my_df["HDL>60"].dtype == bool` reveals that the expected dtype is boolean. Students might figure out this requirement by examining test cell patterns.

**Suggestion:** This is acceptable for autograding but consider if this level of specificity is intended to be hidden.

### Minor Issues

1. **Inconsistent use of `noqa` comments:** The function definitions use `# noqa: N802, N803` to suppress linting warnings about function/parameter naming, but this could confuse students about naming conventions.

2. **Problem 5b mentions "accuracies ranging from approximately 71% to 80%"** in the solution, but actual values may differ. Free-response solutions should be more general.

3. **Problem 6b solution references "C=1 to 10000"** but the actual best range depends on the data and run. Solutions to interpretation questions should be less specific.

4. **No import for `accuracy_score` at the top:** Cell 55 imports `accuracy_score` mid-notebook. All imports should ideally be at the top for clarity.

5. **Cell 57 displays `l2_results` redundantly** after Problem 6a already displays it. Consider removing or making it part of the test cell.

6. **Problem header "Problem 5a: Execution"** is vague; "Run K-Fold CV" would be clearer.

7. **The link in the bias-variance section** goes to Stack Exchange, which may not be a stable long-term reference. Consider linking to textbook or course materials.

8. **Variable naming:** `missclass` could be `misclassification_rates` for clarity; `aurocs` could be `auroc_scores`.

### Strengths

1. **Excellent pedagogical structure:** The assignment progresses logically from explaining CV concepts with worked examples, to implementing CV by hand, to using sklearn utilities, to applying CV for hyperparameter tuning.

2. **Good balance of theory and practice:** The assignment includes conceptual questions (5b, 6b, 7b, 7c) that require students to understand why they're doing each step, not just how.

3. **Comprehensive worked example:** The "K-Fold CV by Hand" section provides excellent scaffolding before students implement their own functions.

4. **Real-world dataset:** Using NHANES health data makes the classification task meaningful and relatable.

5. **Proper test cell structure:** All test cells follow the format with assertions, error messages, hidden tests, and success messages.

6. **Good use of links to documentation:** The assignment links to sklearn documentation for both the stratification rationale and LogisticRegression parameters.

7. **Bias-variance discussion:** The explanation of why K matters in K-fold CV and the linked resource provide valuable conceptual depth.

8. **Consistent formatting:** Problem headers, solution markers, and code style are consistent throughout.

### Recommendations

1. **Fix the KNN `weights` parameter inconsistency** between Problems 8-10. This is a methodological error that will confuse students and produce incorrect final models.

2. **Add data setup instructions** at the beginning of the assignment specifying where the NHANES files should be located, or add a code cell that downloads them.

3. **Consider using StratifiedKFold** in the KFoldCV function (Problem 4) to maintain consistency with the stratification reasoning introduced in Problem 3, or explicitly discuss why regular KFold is acceptable for the CV step.
---
