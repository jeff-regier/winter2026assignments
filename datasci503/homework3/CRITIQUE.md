---
## Critique: DATASCI 503, Homework 3: Logistic Regression

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Problem 2 appears in a Logistic Regression assignment but covers KNN**
   - **Location**: Problem 2 (cell-5, cell-6)
   - **Description**: Problem 2 is entirely about the curse of dimensionality in K-nearest neighbors (KNN), which is unrelated to logistic regression.
   - **Why problematic**: This creates topic drift and confuses the learning objectives. Students expecting to practice logistic regression are instead solving a KNN problem. The assignment introduction explicitly states this covers "the mathematical foundations of logistic regression" but then includes an unrelated algorithm.
   - **Suggested fix**: Either remove Problem 2 and renumber subsequent problems, or replace it with a logistic regression problem (e.g., analyzing logistic regression coefficients, regularization effects, or multi-class classification).

2. **Problem 4 solution contains an error/inconsistency that could confuse students**
   - **Location**: Problem 4, part (c) solution (cell-10)
   - **Description**: The solution derives the correct relationship but then "verifies" with values that don't match, stating the models "differ." However, the problem asks students to "show the relationship," implying the values should work. The problem setup appears intentionally designed with mismatched coefficients without explaining why.
   - **Why problematic**: Students may be confused about whether they made an error. The problem should either: (a) use coefficients that actually satisfy the relationship to demonstrate equivalence, or (b) explicitly ask students to verify whether the two models are equivalent.
   - **Suggested fix**: Revise part (c) to ask: "Show the general relationship between the coefficients. Then verify whether my friend's model is equivalent to mine given the specific coefficient values." This makes the mismatch intentional and pedagogically valuable.

### Moderate Issues

1. **Missing data files warning**
   - **Location**: Problem 6-11 (cell-16)
   - **Description**: The assignment loads CSV files from `./data/college_train.csv` and `./data/college_test.csv` without providing context about the dataset or ensuring students have the files.
   - **Suggestion**: Add a markdown cell describing the College dataset (what features it contains, what "Private" means, source of the data) and confirm the data files are provided in the assignment distribution.

2. **Problem 7 hint may be misleading about log_loss behavior**
   - **Location**: Problem 7 (cell-21)
   - **Description**: The hint says to use `sklearn.metrics.log_loss()` to compute NLL, but `log_loss` returns the mean cross-entropy loss, not the total NLL. The problem says "mean NLL" which is correct, but students may confuse NLL with log_loss.
   - **Suggestion**: Clarify that `log_loss` computes the average negative log-likelihood (cross-entropy loss) across all samples.

3. **Problem 8-9 use inconsistent methods for computing metrics**
   - **Location**: Problems 8 and 9 (cell-25, cell-28)
   - **Description**: Problem 8 solution uses confusion matrix elements directly, while Problem 9 uses `sklearn.metrics.recall_score`. Students should learn one consistent approach.
   - **Suggestion**: Use the same method in both solutions, preferably the confusion matrix approach for pedagogical clarity, or introduce `sklearn.metrics` functions earlier with explanation.

4. **Problem 9 lacks explicit answer to the comparison question**
   - **Location**: Problem 9 (cell-27, cell-28)
   - **Description**: The problem asks "What happens to TPR and FPR when we increase the threshold?" but the solution only prints values without answering this conceptual question.
   - **Suggestion**: Add a free-response section or include a print statement in the solution explaining that increasing the threshold decreases both TPR and FPR (the model becomes more conservative in predicting the positive class).

5. **Problem 10 manual ROC implementation when sklearn has built-in function**
   - **Location**: Problem 10 (cell-30, cell-31)
   - **Description**: Students manually compute ROC curve points when `sklearn.metrics.roc_curve()` exists. While manual implementation has pedagogical value, the assignment doesn't explain why this approach is used.
   - **Suggestion**: Either explain that manual implementation helps understand the concept, or add a follow-up comparing the manual result to `sklearn.metrics.roc_curve()` output.

6. **Hidden test thresholds may be too strict**
   - **Location**: Problems 8, 11 (cell-26, cell-35)
   - **Description**: Hidden tests require `tpr > 0.9`, `fpr < 0.15`, and `auc > 0.95`. These depend heavily on the specific train/test split and model hyperparameters.
   - **Suggestion**: Either provide a fixed random seed for reproducibility or loosen the thresholds slightly (e.g., `tpr > 0.85`, `auc > 0.90`).

### Minor Issues

- **Problem 1**: Uses uppercase $X$ inconsistently (sometimes data, sometimes random variable). Consider lowercase $x$ for observed values.
- **Problem 3**: Could include a hint about the formula for converting between odds and probability: $p = \frac{\text{odds}}{1 + \text{odds}}$.
- **Problem 5**: The phrase "5 hours per week" is unusual for study time (typically "per week" isn't needed for this type of problem). Consider simplifying to "studies for 5 hours."
- **Cell 13**: The verification code for Problem 5 is instructor-provided, not a student solution. Consider moving it after the solution cell or removing it to avoid confusion.
- **Problem 10 test cell**: The assertion `fpr_list[0] == 1.0 or tpr_list[0] == 1.0` should be `and` not `or` since at threshold 0, all predictions are positive (TPR=1, FPR=1).

### Strengths

- **Strong theoretical foundation**: Problems 1, 3-5 build solid conceptual understanding of odds, log-odds, probability, and the connection between logistic and softmax regression.
- **Good progression**: The assignment moves logically from theory (Problems 1-5) to application (Problems 6-11).
- **Practical skills**: The applied section covers essential ML workflow: training, evaluation, and ROC/AUC analysis.
- **Clear test structure**: Test cells follow the required format with visible assertions, descriptive messages, and hidden tests for autograding.
- **Helpful hints**: Problems 7, 10, and 11 include useful hints pointing to relevant sklearn functions.
- **Solution markers properly formatted**: All problems use correct BEGIN/END SOLUTION markers.

### Recommendations

1. **Remove or replace Problem 2** to maintain focus on logistic regression. If KNN content is important for the course, move it to a separate assignment about non-parametric methods.

2. **Add dataset description** before Problem 6, explaining the College dataset features and the classification task. This contextualizes the applied problems.

3. **Fix Problem 4's ambiguity** by explicitly asking students to verify whether the two models are equivalent, making the coefficient mismatch a deliberate learning point rather than a source of confusion.
---
