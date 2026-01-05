---
## Critique: Group Work 6: Regularizing Neural Networks

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Hidden tests are placeholders with no actual assertions**
   - **Location**: cells 17, 22, 27, 33, 38, 43, 48 (all `# BEGIN HIDDEN TESTS` sections for Problems 2a-3c)
   - **Description**: The hidden test sections contain only comments like `# Verify model structure for 2a` but no actual assertions that verify the model architecture.
   - **Why problematic**: These tests will pass for any `nn.Module`, allowing students to submit incorrect architectures (wrong layer widths, wrong number of layers, missing activation functions) and still receive full credit.
   - **Suggested fix**: Add concrete assertions that verify model structure. For example:
     ```python
     # BEGIN HIDDEN TESTS
     layers = list(model.children())
     assert len(layers) == 3, "Expected 3 layers (Linear, ELU, Linear)"
     assert isinstance(layers[0], nn.Linear), "First layer should be Linear"
     assert layers[0].in_features == 28, "Input dimension should be 28"
     assert layers[0].out_features == 16, "Hidden layer width should be 16"
     assert isinstance(layers[1], nn.ELU), "Should use ELU activation"
     assert isinstance(layers[2], nn.Linear), "Last layer should be Linear"
     assert layers[2].out_features == 2, "Output dimension should be 2"
     # END HIDDEN TESTS
     ```

2. **File extraction path mismatch may cause FileNotFoundError**
   - **Location**: cell 6
   - **Description**: The code extracts to `"."` (current directory) but expects the file at `"data/HIGGS.csv.gz"`. If the zip contains `HIGGS.csv.gz` at its root, extraction to `"."` will place it in the current directory, not in `data/`.
   - **Why problematic**: Students may encounter confusing file-not-found errors depending on the zip file structure. The extraction destination should match the expected file path.
   - **Suggested fix**: Extract to `"data/"` directory, or verify the actual structure of the zip file and adjust paths accordingly:
     ```python
     zip_ref.extractall("data/")
     ```

### Moderate Issues

1. **Missing data directory creation**
   - **Location**: cell 6
   - **Description**: The code assumes a `data/` directory exists for downloading/extracting files, but never creates it.
   - **Suggestion**: Add `Path("data").mkdir(exist_ok=True)` before the download step.

2. **Unused dataloader variable**
   - **Location**: cell 8
   - **Description**: The variable `dataloader` is created but only used in cell 10 to show one batch histogram. This is confusing given that `train_loader` and `val_loader` are the ones used throughout.
   - **Suggestion**: Rename to `full_dataloader` or add a comment explaining its purpose is just for visualization.

3. **Test cells do not verify weight_decay is actually used in Problem 3a**
   - **Location**: cell 38
   - **Description**: The visible and hidden tests only check that a model exists, not that the optimizer uses weight decay.
   - **Suggestion**: Add a hidden test that inspects the optimizer's param_groups:
     ```python
     assert optimizer.param_groups[0].get('weight_decay', 0) > 0, "Should use weight_decay"
     ```

4. **Test cells do not verify Dropout layers in Problems 3b and 3c**
   - **Location**: cells 43, 48
   - **Description**: Students could submit models without any Dropout layers and still pass the tests.
   - **Suggestion**: Add assertions that check for Dropout layers:
     ```python
     dropout_layers = [m for m in model.modules() if isinstance(m, nn.Dropout)]
     assert len(dropout_layers) >= 3, "Should have Dropout after each hidden layer"
     ```

5. **Problem 2b test cell comes after the model definition but before training**
   - **Location**: cells 21-23
   - **Description**: The test cell (22) is placed between model definition (21) and training (23). This breaks the pattern established in other problems where testing happens after training.
   - **Suggestion**: Move test cell after training, or at least add a comment explaining the structure is intentional.

6. **Broken relative link to data augmentation notebook**
   - **Location**: cell 52 (Conclusions)
   - **Description**: Link to `../images/data_augmentation.ipynb` likely does not exist in the repository structure.
   - **Suggestion**: Either create the referenced notebook, link to an external resource, or remove the link.

### Minor Issues

- **Inconsistent problem header format**: Problem 1 uses "### Problem 1: Write a Training Function" but later problems use "### Problem 2a: Tiny Model" format. Consider using consistent naming like "Problem 2.1" or "Problem 2a" throughout.

- **Variables `train_loss` and `val_loss` referenced before assignment in edge case**: If `train_loader` or `val_loader` are empty, the print statement at line `if epoch % 10 == 0` would fail because `train_loss` and `val_loss` would be undefined. This is unlikely but worth initializing.

- **Missing type hints**: The `train_model` function would benefit from type hints for clarity: `def train_model(model: nn.Module, ...) -> tuple[list[float], list[float]]`.

- **Histogram visualization uses only first batch**: Cell 10 shows histogram of only the first batch, which may not represent the full data distribution well. Consider sampling across multiple batches or using the full dataset.

- **No seed setting for reproducibility**: The `random_split` in cell 8 uses random splits without a generator seed, making results non-reproducible across runs.

### Strengths

1. **Excellent pedagogical progression**: The assignment builds systematically from understanding overfitting to implementing increasingly complex regularization strategies.

2. **Strong conceptual explanations**: The introduction to overfitting/underfitting and the explanations of L1/L2 regularization and dropout are clear and informative.

3. **Good use of visualization**: Each model's training is followed by a loss curve plot, helping students understand the impact of architectural choices.

4. **Real-world dataset**: Using the Higgs dataset provides authentic experience with a large-scale physics dataset.

5. **Proper separation of solution and test cells**: The assignment correctly follows the convention of keeping solutions and tests in separate cells.

6. **Appropriate scaffolding**: Students receive boilerplate code for data loading and plotting, letting them focus on the core learning objectives.

7. **External documentation links**: Good references to PyTorch optimizer documentation and Google ML glossary for L1/L2 regularization.

### Recommendations

1. **Priority 1**: Implement actual hidden tests that verify model architectures. This is essential for autograding to function correctly. Each model specification (layer count, widths, activation functions, dropout) should be verified programmatically.

2. **Priority 2**: Fix the file extraction path issue and add data directory creation. This will prevent students from encountering environment-specific file errors.

3. **Priority 3**: Add assertions that verify the regularization techniques are actually applied (weight_decay in optimizer, Dropout layers in model). Without these, students can pass tests without implementing the required techniques.
---
