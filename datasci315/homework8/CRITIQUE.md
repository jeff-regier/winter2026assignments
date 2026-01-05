---
## Critique: Homework 8 - Fashion MNIST with Regularization

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

#### 1. Visible Tests Reveal Solutions (Problems 1, 2)
**Location:** Test cells for Problems 1 and 2

**Description:** The visible test assertions explicitly state the expected behavior in ways that guide students toward the solution. For example:
- Problem 1: `training_losses_1[-1] > 1.0` and `abs(training_losses_1[-1] - val_losses_1[-1]) < 0.1` directly tell students what loss values to target
- Problem 2: `training_losses_2[-1] < val_losses_2[-1]` and `training_losses_2[-1] < 0.3` reveal the expected loss relationship

**Why problematic:** Students can reverse-engineer the solution from the test conditions rather than understanding why underfitting/overfitting occur. The tests are essentially specifications that make the problem trivially solvable by trial and error.

**Suggested fix:** Move specific numeric thresholds to hidden tests. Visible tests should check structural properties only (e.g., "model is defined", "optimizer is created") or use vague messages like "Your model does not exhibit the expected underfitting behavior."

#### 2. Test Assertions May Fail Non-Deterministically
**Location:** All test cells

**Description:** Due to random weight initialization and random batch ordering, the exact loss values can vary between runs. Assertions like `training_losses_1[-1] > 1.0` or `abs(training_losses_1[-1] - val_losses_1[-1]) < 0.1` may pass or fail depending on random seed.

**Why problematic:** Students might have a correct solution that occasionally fails tests, or an incorrect solution that occasionally passes. This is frustrating and undermines confidence in the autograder.

**Suggested fix:** Either:
1. Set a random seed at the start of the notebook for reproducibility
2. Use wider tolerance thresholds that account for variance
3. Test over multiple runs and check that conditions hold on average

### Moderate Issues

#### 1. Missing Conceptual Questions
**Location:** Throughout assignment

**Description:** The assignment focuses entirely on implementation without requiring students to explain their understanding. Students could complete the entire assignment by copying hints without understanding why different architectures cause underfitting/overfitting.

**Suggestion:** Add follow-up questions after Problems 1-2 asking students to explain in their own words why their model underfits/overfits. Problem 8 is a good start but comes too late.

#### 2. Inconsistent Gap Threshold in Problem 1
**Location:** Problem 1 description vs. test cell

**Description:** The problem description says "within 0.05" but the test checks `< 0.1`. This inconsistency is confusing.

**Suggestion:** Align the problem description and test assertion to use the same threshold.

#### 3. Problem 3 Lacks Complete Specification
**Location:** Problem 3 description

**Description:** The early stopping implementation description mentions `min_delta` should be used for improvement detection, but doesn't clearly specify whether "improvement" means `val_loss < best_val_loss - min_delta` or `best_val_loss - val_loss > min_delta`. Students might implement it differently.

**Suggestion:** Add a concrete example: "For example, if `best_val_loss = 0.5` and `min_delta = 0.01`, then a validation loss of 0.48 would count as improvement (since 0.48 < 0.5 - 0.01 = 0.49), but 0.495 would not."

#### 4. Problems 4-7 Are Too Similar
**Location:** Problems 4, 5, 6, 7

**Description:** All four problems follow the same pattern: copy Problem 2's architecture, add one regularization technique, train, and observe. The hints essentially give away the solution each time. This becomes repetitive and less educational.

**Suggestion:** Consider:
- Combining some problems (e.g., "Try at least two different regularization techniques and compare them")
- Removing hints from later problems to encourage independent exploration
- Adding a problem where students must tune hyperparameters without hints

#### 5. Problem 7 Tests Are Too Weak
**Location:** Problem 7 test cell

**Description:** The tests only check that `val_losses_7[-1] < 0.7` and `training_losses_7[-1] > 0.4`. These don't actually verify that both L2 and dropout are being used together. A student could use only one technique and still pass.

**Suggestion:** Add hidden tests that verify the model contains dropout layers and the optimizer has non-zero weight_decay.

### Minor Issues

- **Missing documentation links:** No links to PyTorch documentation for `nn.Dropout`, `weight_decay`, or related concepts.
- **No seed for reproducibility:** Random split and weight initialization make results non-reproducible. Consider adding `torch.manual_seed(42)`.
- **Problem 8 format:** Uses blockquote solution markers correctly but could benefit from structured prompts (e.g., "Which model? Why? What are the tradeoffs?").
- **No explanation of batch sizes:** The code uses batch_size=256 for training and 1024 for validation without explaining why.
- **Missing import check:** If students haven't run the setup cells, later cells will fail with confusing errors. Consider adding an early sanity check.
- **Inconsistent variable naming:** `training_losses` vs `train_loss` within functions; `val_losses` vs `validation_losses` across functions.

### Strengths

1. **Clear learning objectives:** The assignment has a coherent theme exploring underfitting, overfitting, and regularization techniques.
2. **Good scaffolding:** Providing the training function and plot function lets students focus on model architecture.
3. **Progressive difficulty:** Problems build logically from demonstrating problems (1-2) to solutions (3-7) to synthesis (8).
4. **Practical techniques:** All regularization methods covered (early stopping, model size, L2, dropout) are commonly used in practice.
5. **Proper solution markers:** All solution markers follow the required format.
6. **Model comparison section:** The final comparison code is excellent for helping students see the big picture.
7. **Good introductory context:** The Fashion MNIST description provides useful background.

### Recommendations

1. **Fix non-deterministic tests:** Add `torch.manual_seed(42)` and `random.seed(42)` at the start of the notebook, or use much wider tolerance thresholds that will pass reliably.

2. **Move solution-revealing assertions to hidden tests:** Keep visible tests minimal (e.g., checking that variables exist and have correct types) and put numeric thresholds in hidden tests with vague error messages.

3. **Add conceptual questions:** After Problems 1 and 2, add markdown cells asking students to explain in their own words why their model exhibits underfitting/overfitting behavior. This ensures understanding beyond just copying hints.
---
