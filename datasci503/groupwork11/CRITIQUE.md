---
## Critique: DATASCI 503, Group Work 11: Building and Tuning Neural Networks in PyTorch

### Summary
- **Critical issues**: 3
- **Moderate issues**: 7
- **Minor issues**: 8

### Critical Issues

#### 1. Test Cell Before Solution Code (Problem 6a)
**Location**: cell-40 (test assertions) appears before cell-41 (solution code)
**Description**: The test assertions cell for Problem 6a checks that `model`, `optimizer`, and `weight_decay` are set correctly, but this test cell appears BEFORE the solution code cell where these variables are defined.
**Why problematic**: Students cannot run the notebook sequentially. The test will fail because `model` and `optimizer` are not yet defined (or will reference the wrong model from a previous problem).
**Suggested fix**: Move cell-40 to after cell-41, so the test assertions come after the solution code.

#### 2. Test Cell Checks Wrong Conditions (Problem 6b and 6c)
**Location**: cell-44 (tests dropout for 6b), cell-52 (tests regularization for 6c)
**Description**:
- cell-44 tests for dropout, but it appears BEFORE the Problem 6b section header (cell-45) and solution code (cell-46).
- cell-52 tests for "at least one regularization technique" but the problem 6c is about early stopping, not regularization.
**Why problematic**: Test cells are misaligned with their problems. The tests will fail or check incorrect conditions for the actual problem.
**Suggested fix**:
- Move cell-44 to after cell-46 and the training cell-47
- Rewrite cell-52 to check for early stopping usage rather than weight decay/dropout

#### 3. Hidden Test References Undefined Variable
**Location**: cell-44 hidden tests
**Description**: The hidden test `assert len(dropout_layers) == n_hidden` references `n_hidden`, but this variable is defined in cell-46 (the solution code), which comes AFTER the test cell due to the ordering issue.
**Why problematic**: This will cause a NameError when running hidden tests.
**Suggested fix**: Either define `n_hidden` in the test cell itself, or fix the cell ordering so the solution defines it first.

### Moderate Issues

#### 1. Missing Test Cells for Multiple Problems
**Location**: Problem 3, Problem 5b, Problem 6c training
**Description**:
- Problem 3 has tests but they only check split sizes, not that shuffling with stratification was actually used.
- Problem 5b has no test assertions cell at all.
- Problem 6c's training in cell-53 has no test to verify early stopping actually occurred.
**Suggested fix**: Add test cells that verify:
- Problem 3: Check stratification maintained class ratios
- Problem 5b: Check that at least 8 model configurations were tested
- Problem 6c: Check that `len(training_losses) < 200`

#### 2. Data File Path Not Documented
**Location**: cell-18
**Description**: The code loads from `"data/higgs.csv"` but there's no indication to students where this file comes from or how to obtain it.
**Suggested fix**: Add a note explaining where the data file should be located or how to download it.

#### 3. Problem 5b Test Loss vs Validation Loss Confusion
**Location**: cell-35
**Description**: The problem asks students to "record the final validation loss" but then asks to "print out the test loss of the best performing model." The solution computes test loss on `X_test` but this is evaluating directly without using the test_loader and without proper batching for large datasets.
**Suggested fix**: Clarify the distinction between validation and test sets. Have students use the test_loader for proper evaluation.

#### 4. Inconsistent Shuffle Behavior in DataLoaders
**Location**: cell-21
**Description**: The solution sets `shuffle=True` for validation and test DataLoaders, but validation and test sets should typically not be shuffled as it provides no benefit and can cause confusion during evaluation.
**Suggested fix**: Use `shuffle=False` for validation and test loaders.

#### 5. Missing Seed for Reproducibility in Problem 5b
**Location**: cell-34
**Description**: Problem 5b trains 8 models but doesn't set a random seed before training each model, making results non-reproducible.
**Suggested fix**: Set `torch.manual_seed(42)` before training each model for reproducibility.

#### 6. Problem 6 Parts Share Model Variables
**Location**: Problems 6a, 6b, 6c, 6d
**Description**: Each part reuses the variable names `model`, `criterion`, `optimizer` without clearing previous state. The test in cell-58 checks for early stopping (`len(training_losses) < 500`) but this will reference the results from Problem 6d, not verify the student's work.
**Suggested fix**: Use distinct variable names for each sub-problem or add comments clarifying that variables will be overwritten.

#### 7. Cross-Entropy Loss Output Dimension Explanation Missing
**Location**: Throughout (models use `output_dim=2` for binary classification)
**Description**: Students might not understand why binary classification uses 2 output neurons with CrossEntropyLoss instead of 1 output neuron with BCEWithLogitsLoss.
**Suggested fix**: Add a brief explanation of the two approaches to binary classification in PyTorch.

### Minor Issues

- **cell-3**: The note about random state 42 appears but `torch.manual_seed(42)` is not consistently used throughout the notebook.
- **cell-6**: The list format "2. List item" through "5. List item" is awkward starter text; could use numbered placeholders with descriptions.
- **cell-15**: Minor typo: "wiith" should be "with".
- **cell-18**: Column renaming logic is confusing - the label column is named but then renamed via a comprehension that includes it.
- **cell-23**: A cell containing only `len(validation_loader)` has no explanatory purpose; consider adding a comment or removing.
- **cell-36**: The example solution mentions "test loss of approximately 0.0058" which is suspiciously low for cross-entropy loss on a classification task (should be around 0.5-0.7).
- **cell-60**: A cell containing only `validation_losses` at the end serves no purpose; consider removing.
- **cell-61**: Empty cell at the end should be removed.

### Strengths

1. **Comprehensive Coverage**: The assignment covers fundamental neural network concepts including activation functions, loss functions, gradient descent, DataLoaders, model architecture search, and multiple regularization techniques.

2. **Well-Documented Training Function**: The `train_model` function in cell-25 is thoroughly commented, explaining each step of the training loop which is excellent for pedagogical purposes.

3. **Progressive Complexity**: The assignment builds logically from basic concepts (activation functions, loss functions) to implementation (gradient descent with autograd) to practical application (model comparison, regularization).

4. **Practical Tips**: The "Tips and Tricks" section (cell-15) and the regularization explanations (cell-39) provide useful context beyond the immediate problems.

5. **Reasonable Scope**: The assignment gives students hands-on experience with the full neural network training pipeline without being overwhelming.

6. **Good Use of Visualizations**: Plotting training and validation loss curves helps students understand model behavior.

### Recommendations

**Top 3 Priority Fixes:**

1. **Fix cell ordering in Problem 6**: The test cells (cell-40, cell-44, cell-52) are misplaced relative to their solution cells. Reorder so test assertions always follow the code they test.

2. **Add missing test cells**: Problem 5b needs assertions verifying that students tested at least 8 configurations and recorded results. Problem 6c needs verification that early stopping actually triggered.

3. **Fix hidden test variable reference**: The hidden test in cell-44 references `n_hidden` which won't be defined at test execution time. Either fix the cell order or hardcode the expected value.
---
