---
## Critique: Homework 7 - Regularization for Image Classification

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

#### 1. Optimizer State Not Reset When Re-training
- **Location**: Problem 2, cells 20-25
- **Description**: The `reset_model_parameters()` function resets model weights, but when students iterate on hyperparameters and re-run training, the optimizer object retains stale momentum/state from the previous run. The optimizer is created once (cell 25) with `model.parameters()`, and if students change `lr` or `weight_decay` and re-run only the training cell, the optimizer still uses old hyperparameters.
- **Why problematic**: Students may be confused when changing hyperparameters appears to have no effect, or when training behaves unexpectedly due to stale optimizer state. This defeats the purpose of experimenting with regularization.
- **Suggested fix**: Either (1) recreate the optimizer inside the `train()` function, (2) add a helper function to reset optimizer state, or (3) add clear instructions that students must re-run the optimizer cell when changing hyperparameters.

#### 2. Data Files May Not Exist - No Graceful Error Handling
- **Location**: Cell 6
- **Description**: The code assumes `data/dataset_train_0.5_norm.pt` and `data/dataset_test_0.5_norm.pt` exist. If students haven't downloaded the files or placed them incorrectly, they get a cryptic `FileNotFoundError`.
- **Why problematic**: Students unfamiliar with file paths may struggle to debug. The Canvas download links in the instructions may break over time, and there's no verification step.
- **Suggested fix**: Add a try-except block with a helpful error message directing students to the download instructions, or add a cell that checks if files exist before loading.

### Moderate Issues

#### 1. Problem 1 Lacks Guidance on Architecture Design
- **Location**: Cell 15-16
- **Description**: Students are told to "fill out the below with a model architecture that you think will work well" with no guidance on layer sizes, depth, or dropout placement. The only hint is a link to dropout documentation.
- **Suggestion**: Provide rough guidance (e.g., "consider 2-4 hidden layers with 128-512 units each") or a scaffold with placeholders like `nn.Linear(dim*dim, ???)`. This is a homework on regularization, not architecture search.

#### 2. Problem 2 Training Function Lacks Specification
- **Location**: Cell 21-22
- **Description**: The function signature and expected behavior are not specified. Students don't know: (1) what loss function to use, (2) whether to return losses per epoch or cumulative, (3) whether to print progress, (4) expected return type.
- **Suggestion**: Provide a docstring template or explicit requirements: "Use CrossEntropyLoss. Return lists of per-epoch average losses. Print epoch progress."

#### 3. Test for `train()` Function is Weak
- **Location**: Cell 23
- **Description**: The test only checks that `train` is callable and has at least 4 parameters. It doesn't verify the function actually trains or returns the correct format.
- **Suggestion**: Add a hidden test that runs training for 1 epoch on a small subset and verifies returned loss lists have the correct length and are non-empty.

#### 4. Visible Test in Cell 38 May Give Away Solution Format
- **Location**: Cell 38
- **Description**: The visible assertion `assert test_accuracy >= 0.63` implies students must compute `test_accuracy` as a float. While the solution code is marked, students see this test in the student version.
- **Suggestion**: This is borderline acceptable since the variable name is intuitive, but consider making the accuracy computation scaffolded or move the check to hidden tests.

#### 5. No Explanation of L2 Regularization / weight_decay
- **Location**: Cell 21, 24-25
- **Description**: The assignment mentions `weight_decay` "uses L2 regularization to penalize large weights" but doesn't explain what L2 regularization is or why it helps. This is a homework on regularization, so conceptual understanding matters.
- **Suggestion**: Add a brief explanation or link to documentation. Consider adding a question asking students to explain why weight decay helps.

#### 6. Batch Size Cell Has Mixed Student/Solution Content
- **Location**: Cell 28
- **Description**: `batch_size = 256 # SOLUTION` but the rest of the cell (DataLoader setup) is not marked as solution. This means students will see the DataLoader code but must fill in batch_size. This is fine, but the cell structure could be clearer.
- **Suggestion**: Either mark the entire cell as solution or separate the batch_size definition from the DataLoader setup.

### Minor Issues

- **Cell 7**: The 90/10 train/validation split is hardcoded. Consider explaining why this split ratio is chosen.
- **Cell 11**: The markdown says "test set" but displays a validation image. The cell uses `val_images`, not `test_images`.
- **Problem headers**: Problems use `## Problem N` format instead of the conventional `### Problem N: Title` format specified in CLAUDE.md.
- **Cell 37**: The accuracy computation is inside a BEGIN/END SOLUTION block, but computing accuracy from predictions is a learning objective. Consider scaffolding this with hints about `argmax`.
- **No success print statements**: Test cells don't include `print("All tests passed!")` as specified in the conventions.

### Strengths

1. **Clear learning objective**: The assignment has a focused goal (achieving 63% accuracy using regularization) that ties together the concepts.
2. **Good scaffolding for data loading**: The train/val/test split is provided, reducing boilerplate and letting students focus on the model.
3. **Appropriate use of visualization**: Displaying sample images helps students understand the data.
4. **Progressive structure**: The assignment flows logically from model definition to training to evaluation.
5. **Practical regularization techniques**: Introduces both dropout and weight decay, which are fundamental techniques.
6. **Reasonable target accuracy**: 63% is achievable but requires thoughtful regularization choices.

### Recommendations

1. **Priority 1**: Fix the optimizer state issue by either recreating the optimizer inside `train()` or adding explicit instructions about re-running the optimizer cell when changing hyperparameters.

2. **Priority 2**: Add more guidance to Problem 1 about model architecture. Provide a scaffold or suggested range of hyperparameters so students can focus on regularization rather than architecture search.

3. **Priority 3**: Specify the `train()` function requirements explicitly (loss function, return format, expected behavior) and strengthen the hidden tests to verify the function works correctly.
---
