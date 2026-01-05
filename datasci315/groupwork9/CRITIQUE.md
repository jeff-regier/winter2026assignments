---
## Critique: Groupwork 9 - Kaggle Galaxy Challenge with CNNs

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Missing Test Cell for Problem 3 DataLoader Configuration**
   - **Location:** Cell 28 (after batch_size test in cell 26)
   - **Description:** Problem 3 requires students to configure both the optimizer/batch_size AND the data loaders. The test cell in cell 26 only tests the optimizer and batch_size, but there is no test cell for the data loader configuration in cell 28.
   - **Why problematic:** The `# BEGIN SOLUTION` / `# END SOLUTION` block in cell 28 contains critical code (including a custom `AugmentedGalaxyDataset` class) that lacks any validation. Students could implement this incorrectly without receiving feedback. The autograder will not check if `train_dataloader` and `val_dataloader` are properly defined.
   - **Suggested fix:** Add a test cell after cell 28:
     ```python
     # Test assertions
     assert train_dataloader is not None, "train_dataloader must be defined"
     assert val_dataloader is not None, "val_dataloader must be defined"
     assert hasattr(train_dataloader, '__iter__'), "train_dataloader must be iterable"
     print("All tests passed!")

     # BEGIN HIDDEN TESTS
     batch = next(iter(train_dataloader))
     assert len(batch) == 2, "dataloader should yield (images, labels) tuples"
     assert batch[0].shape[1] == 1, "images should have 1 channel"
     # END HIDDEN TESTS
     ```

2. **Problem Header Non-Conformance**
   - **Location:** Cells 16, 20, 24, 29 (Problem headers)
   - **Description:** Problem headers use `### Problem N: Title` format but some are inconsistent with the structural conventions. Specifically, Problem 3 and Problem 4 lack clear delineation since Problem 3's solution spans multiple cells (cells 25 and 28).
   - **Why problematic:** Problem 3 is split across two non-contiguous solution blocks (cell 25 for optimizer/batch_size, cell 28 for dataloaders), which violates the expectation that each problem is self-contained. This makes grading confusing and could cause issues with the student version generator.
   - **Suggested fix:** Split Problem 3 into two separate problems: "Problem 3: Configure Optimizer and Batch Size" and "Problem 4: Create Data Loaders", then renumber subsequent problems.

### Moderate Issues

1. **Mismatch Between Problem Requirements and Tests**
   - **Location:** Cell 29 (Problem 4) and Cell 35 (test assertions)
   - **Description:** Problem 4 states students must achieve "at least 90% accuracy" on validation, but the test only requires `val_accuracy >= 0.75` (75%).
   - **Suggestion:** Either lower the stated requirement to 75% or increase the test threshold to 0.90 to match the problem description. Given this is a learning exercise, 75% may be more appropriate.

2. **Potential Solution Giveaway in Problem 1 Hint**
   - **Location:** Cell 16
   - **Description:** The hint "Conv -> ReLU -> Pool -> Conv -> ReLU -> Pool -> Flatten -> FC -> ReLU -> FC" essentially gives away the architecture pattern, making the "design" aspect trivial.
   - **Suggestion:** Make the hint more general, e.g., "Consider stacking convolutional blocks (each with convolution, activation, and pooling) followed by fully connected layers."

3. **Missing Documentation Link for CosineAnnealingLR**
   - **Location:** Cell 22 (solution uses `CosineAnnealingLR`)
   - **Description:** The solution uses `CosineAnnealingLR` which is imported at the top but never explained. Students may not understand this learning rate scheduler.
   - **Suggestion:** Either remove it from the solution (use a simpler approach) or add a brief explanation and documentation link for students who want to explore it.

4. **Complex Solution in Problem 3 Beyond Requirements**
   - **Location:** Cell 28
   - **Description:** The solution implements a custom `AugmentedGalaxyDataset` class with data augmentation, but the problem statement only asks students to "set up data loaders." This goes far beyond what's required.
   - **Suggestion:** Either simplify the solution to use basic `TensorDataset` and `DataLoader`, or add data augmentation as an explicit optional extension.

5. **Missing Error Messages in Some Assertions**
   - **Location:** Cells 19, 23, 26, 35
   - **Description:** Some assertions have good error messages, but hidden test assertions lack them entirely.
   - **Suggestion:** Add descriptive error messages to all hidden test assertions for better debugging when students fail.

6. **Kaggle Link May Be Temporary/Broken**
   - **Location:** Cell 1
   - **Description:** The Kaggle competition link `https://www.kaggle.com/t/c7bb7892c2774d61af49f788398b2eec` uses a temporary invite token format that may expire.
   - **Suggestion:** Verify the link is still active. Consider using a permanent competition URL or noting that the link may need to be updated each semester.

### Minor Issues

- **Cell 4:** The device check output could be misleading if students run on CPU but expect GPU performance. Consider adding a warning if CUDA is not available.
- **Cell 7:** File paths are hardcoded to `data/` which may not match all students' setups. Consider adding a note about adjusting paths.
- **Cell 22:** The `reset_model_parameters` function is provided but its purpose isn't explained in the problem description.
- **Cell 34:** Comment says "use batched version if this runs out of memory" but no batched version is provided.
- **Inconsistent epoch printing:** The solution prints with `{epoch:2d}` which assumes < 100 epochs; this is fine but could be more flexible.

### Strengths

1. **Clear learning objectives:** The assignment clearly frames galaxy counting as a classification problem and explains the CNN approach well.
2. **Good scaffolding:** The assignment provides helpful setup code for data loading, visualization, and submission generation.
3. **Practical application:** Using a real Kaggle competition provides authentic motivation and allows students to see how they compare to others.
4. **Visualization support:** Including code to visualize training/validation losses and data distribution helps students understand their model's behavior.
5. **Helpful hints:** Problem descriptions include actionable hints about hyperparameters and architecture choices.
6. **Good imports organization:** All imports are at the top and well-organized.
7. **Reference to PyTorch tutorial:** Linking to the official PyTorch CNN tutorial provides additional learning resources.

### Recommendations

1. **Add missing test cell for data loaders (Critical):** Add a test cell after cell 28 to validate that `train_dataloader` and `val_dataloader` are properly configured.

2. **Fix accuracy requirement mismatch (Moderate):** Align the stated requirement (90%) with the actual test threshold (75%), preferring to update the problem description to say 75% since that's more realistic for beginners.

3. **Restructure Problem 3 (Critical):** Split into two problems to avoid having solution code spread across non-contiguous cells, which improves clarity and makes grading easier.
---
