---
## Critique: Group Work 8 - Convolutional Neural Networks with CIFAR-10

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 4

### Critical Issues

#### 1. External Image Link May Break
- **Location**: Problem 1 (cell-8)
- **Description**: The CNN architecture diagram is hosted on an external WordPress site (`https://i0.wp.com/developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png`). External links can become unavailable, breaking the assignment for future students.
- **Why problematic**: If the image becomes inaccessible, students will have no visual reference for the expected architecture, making the problem significantly harder to understand.
- **Suggested fix**: Either (1) host the image locally in the repository, or (2) provide a complete textual description of the architecture that doesn't rely on the image. The current text description is incomplete - it doesn't specify the pooling layer parameters, activation functions, or the sizes of the fully connected layers (120, 84, 10).

#### 2. Problem 3 Test Cell is Essentially Empty
- **Location**: Problem 3 test assertions (cell-16)
- **Description**: The test assertion `assert "running_loss" in dir() or True` always passes due to the `or True`. The hidden tests section is also empty (just a comment). This provides no validation of the training loop implementation.
- **Why problematic**: Students could submit broken training code (e.g., missing `loss.backward()` or `optimizer.step()`) and still pass all tests. The assertion is a no-op.
- **Suggested fix**: Add meaningful tests such as:
  ```python
  # Verify model parameters have been updated by checking gradients exist
  # or by comparing model weights before/after training
  sample = torch.randn(1, 3, 32, 32)
  with torch.no_grad():
      output = net(sample)
  assert output.shape == (1, 10), "Model should still produce correct output shape after training"
  ```

### Moderate Issues

#### 1. Problem 1 Architecture Specification is Incomplete
- **Location**: Problem 1 (cell-8)
- **Description**: The problem specifies convolutional layer sizes but omits: (1) max pooling parameters (kernel_size=2, stride=2), (2) fully connected layer sizes (400->120->84->10), (3) activation functions (ReLU). Students must infer these from the diagram or guess.
- **Suggestion**: Explicitly list all layer specifications, including pooling parameters and FC layer sizes.

#### 2. Missing ReLU Mention in Problem 1
- **Location**: Problem 1 (cell-8)
- **Description**: The problem mentions "Two convolutional layers followed by max pooling" but doesn't mention activation functions. The solution uses ReLU, but students aren't told this.
- **Suggestion**: Add "Apply ReLU activation after each convolutional layer and after the first two fully connected layers" to the requirements.

#### 3. Problem 2 Lacks Guidance on Learning Rate
- **Location**: Problem 2 (cell-11)
- **Description**: The problem says "Any choice of learning rate is fine for now" but the solution uses `lr=0.001, momentum=0.9`. Poor learning rate choices could lead to not achieving 50% accuracy, causing confusion in Problem 4.
- **Suggestion**: Provide a recommended range (e.g., "A learning rate between 0.001 and 0.01 with momentum around 0.9 works well").

#### 4. Long Training Time Without Warning
- **Location**: Problem 3 (cell-14/15)
- **Description**: Training 2 epochs on CIFAR-10 with batch_size=4 means 25,000 iterations, which can take several minutes on CPU. Students aren't warned about expected runtime.
- **Suggestion**: Add a note like "Training may take 2-5 minutes on CPU. You'll see progress updates every 2000 mini-batches."

#### 5. Hidden Test in Problem 4 Assumes Full Test Set
- **Location**: Problem 4 hidden tests (cell-19)
- **Description**: The hidden test `assert total == 10000` assumes students iterate through all test data exactly once. If a student's implementation has a bug that causes early termination, the hidden test will fail with an uninformative error.
- **Suggestion**: Add a descriptive error message: `assert total == 10000, f"Should evaluate on all 10000 test images, but only evaluated {total}"`

### Minor Issues

- **Problem header format**: Uses `## Problem N:` instead of `### Problem N:` as specified in the conventions.
- **Missing matplotlib import**: The intro mentions "matplotlib for visualization" but matplotlib is never imported or used in the assignment.
- **Variable naming in Problem 5**: Uses `classname` (not snake_case `class_name`), though this is a minor style inconsistency.
- **Batch size comment**: Setting `batch_size = 4` is unusually small and could be explained (it's from the PyTorch tutorial but affects training speed).

### Strengths

1. **Excellent background section**: The explanation of convolutional and pooling layers with the formula for output dimensions is thorough and educational.
2. **Worked example**: Cell-6 and cell-7 provide a concrete example showing how to compute output shapes, which directly helps with Problem 1.
3. **Good documentation links**: Problem 1 links to official PyTorch documentation for Conv2d and MaxPool2d.
4. **Logical flow**: The assignment progresses naturally from defining the network, to training, to evaluation, to per-class analysis.
5. **Appropriate difficulty**: The problems build on each other and the 50% accuracy target is achievable with the given architecture.
6. **Helpful note about CrossEntropyLoss**: Clarifying that softmax is included internally prevents a common student mistake.

### Recommendations

1. **[Critical] Fix the empty test cell for Problem 3** - This is the highest priority as it provides no validation of the core training loop implementation.

2. **[Critical] Complete the architecture specification in Problem 1** - Either host the image locally or provide a complete textual description including pooling parameters, activation functions, and FC layer sizes.

3. **[Moderate] Add expected training time warning** - Help students understand that the training loop will take several minutes and what progress to expect.
---
