---
## Critique: DATASCI 503, Group Work 12: Fashion MNIST with Regularization

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

#### 1. Problem 9 Test Assertions Do Not Verify Implicit Regularization Effect
**Location:** Problem 9, test cell (cell-43)

**Description:** The test assertions for Problem 9 only check that training occurred (loss decreased) and that 50 epochs ran. They do not verify that implicit regularization actually reduced overfitting compared to Problem 2.

**Why problematic:** The problem asks students to modify learning rate and/or batch size to reduce overfitting, but the visible tests do not check whether overfitting was actually reduced. Students could submit code that shows no improvement and still pass the tests.

**Suggested fix:** Add an assertion comparing the validation-training loss gap to the overfitting model:
```python
implreg_gap = implreg_validation_losses[-1] - implreg_training_losses[-1]
assert implreg_gap < overfit_gap, f"Expected implicit regularization to reduce overfitting, got gap {implreg_gap:.3f} vs {overfit_gap:.3f}"
```

#### 2. Hidden Test in Problem 5 May Fail Due to Stochastic Training
**Location:** Problem 5, hidden tests (cell-27)

**Description:** The hidden test asserts `l2_training_losses[-1] > overfit_training_losses[-1]`, expecting L2-regularized training loss to be higher. However, this is not guaranteed due to stochastic training (different random initializations, mini-batch ordering).

**Why problematic:** L2 regularization adds a penalty term, but the actual training loss (without the penalty) could still be lower in some runs. This could cause correct solutions to fail unpredictably.

**Suggested fix:** Either remove this assertion or make it more robust by checking that the regularized model has a smaller gap between training and validation loss (which is already tested in the visible assertions).

### Moderate Issues

#### 1. Problem 1 Hint Potentially Gives Away Solution
**Location:** Problem 1 description (cell-7)

**Description:** The hint explicitly states "Use a very small hidden layer (e.g., 2 neurons)" which essentially gives away the exact solution approach.

**Suggestion:** Provide a more general hint: "Consider what happens when a model has very limited capacity. What architectural choices limit capacity?"

#### 2. Problem 2 Does Not Specify Clear Success Criteria for Overfitting
**Location:** Problem 2 description (cell-11)

**Description:** The problem says validation loss should "begin increasing" but does not specify how much or when. Students may be confused about what constitutes sufficient overfitting.

**Suggestion:** Add more specific guidance: "The validation loss should reach its minimum within the first 30-40 epochs and then increase by at least 0.1 above the minimum by epoch 50."

#### 3. Problem 3 Prints Every Epoch (Verbose Output)
**Location:** Problem 3 solution (cell-16)

**Description:** The `train_model_with_early_stopping` function prints every epoch rather than every 10 epochs like the original `train_model` function. This creates inconsistent, verbose output.

**Suggestion:** Modify the printing to match the original function (every 10 epochs) or make printing configurable via a parameter.

#### 4. Problem 8 Test Assertion Uses `<=` Instead of `<`
**Location:** Problem 8, test cell (cell-39)

**Description:** The assertion uses `len(dropoutearly_training_losses) <= 50` which would pass even if early stopping never triggered. Given that dropout with 0.7 probability may prevent validation loss from improving, early stopping might not trigger.

**Suggestion:** The test should verify that early stopping actually triggered: `assert len(dropoutearly_training_losses) < 50, "Expected early stopping to trigger before 50 epochs"`

#### 5. Problem 10 Free-Response Missing Clear Question
**Location:** Problem 10 (cells 47-48)

**Description:** The question "Which model would you choose for deployment and why?" appears in a separate markdown cell from the solution markers. This creates an awkward structure.

**Suggestion:** Combine the question with the solution markers in a single cell or use the standard free-response format with `### Problem 10b:` header for the written portion.

#### 6. Inconsistent Dropout Placement in Solutions
**Location:** Problems 6, 7, 8 solutions

**Description:** The solutions only add dropout after the first hidden layer, but not after the second. This inconsistency may confuse students about where dropout should be placed.

**Suggestion:** Either explain why dropout is only after the first layer, or add dropout after both hidden layers for consistency. Consider adding a note about common dropout placement strategies.

### Minor Issues

- **Problem 4:** The hint suggests "e.g., 128 neurons per layer" for overfitting (Problem 2) but does not suggest a specific size for the reduced model in Problem 4. Adding "e.g., 32 neurons" would help students.

- **Variable naming:** Some solutions use `inputs, targets` (Problem 3) while others use `batch_x, batch_y`. Consistency would improve readability.

- **Missing device handling:** The code does not move models or data to GPU. While this works on CPU, adding a note about device handling for larger models would be educational.

- **Problem 6 hint:** The hint suggests "p=0.5 or higher" but the solution uses p=0.7. The hint could mention that higher dropout rates provide stronger regularization.

- **Confusion matrix labels:** The confusion matrices in Problem 10 use numeric labels (0-9) rather than class names (T-shirt, Trouser, etc.), making interpretation harder.

### Strengths

1. **Excellent pedagogical progression:** The assignment builds systematically from underfitting to overfitting to various regularization techniques, creating a clear learning arc.

2. **Practical, real-world dataset:** Fashion MNIST is more challenging than MNIST digits and provides a realistic benchmark for students to work with.

3. **Comprehensive coverage:** The assignment covers multiple regularization techniques (early stopping, reduced capacity, L2, dropout, implicit regularization) and their combinations.

4. **Good scaffolding:** Providing the `train_model` function upfront allows students to focus on model architecture and regularization concepts rather than boilerplate training code.

5. **Strong visual component:** Each problem requires plotting training curves, helping students develop intuition about overfitting and regularization effects.

6. **Thoughtful hidden tests:** The hidden tests check for meaningful properties (model capacity, presence of dropout layers, parameter counts) rather than just outputs.

7. **Comparative analysis:** Problem 10 effectively synthesizes all the techniques by comparing models on test data and requiring students to make a reasoned deployment decision.

### Recommendations

1. **Fix Problem 9 test assertions** to actually verify that implicit regularization reduced overfitting compared to the baseline overfitting model. This is critical for ensuring the learning objective is met.

2. **Revise the Problem 5 hidden test** to avoid the stochastic failure mode. Either remove the assertion about training loss or test something more deterministic like the gap between training and validation loss.

3. **Improve hint specificity** to balance guidance with learning opportunity. Hints should guide thinking without giving away exact solutions. For example, Problem 1's hint could ask students to consider model capacity without specifying exactly 2 neurons.

---
