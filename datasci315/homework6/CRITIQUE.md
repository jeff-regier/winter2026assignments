---
## Critique: Homework 6 - Training Models with PyTorch

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

#### 1. Global Variable Dependency in Model Function (Problem 2c)
**Location:** Cell cell-23 (model function definition)

**Description:** The `model` function in Problem 2c references global variables `W1`, `b1`, `W2`, `b2` directly rather than accepting them as parameters. This creates a tight coupling between the model and the specific weight tensors defined in Problem 2b.

**Why problematic:**
- Students cannot test their model function independently of their initialization code
- The model cannot be easily reinitialized or used with different weights
- This design pattern contradicts good software engineering practices and can confuse students about proper function design
- If a student makes an error in Problem 2b, it silently cascades to Problem 2c

**Suggested fix:** Either (1) pass weights as parameters to the model function, or (2) wrap everything in a class structure, or (3) explicitly document this design choice and explain why it's acceptable for this pedagogical context.

#### 2. Inconsistent Model Output Shape (Problem 2c)
**Location:** Cell cell-23 and cell-24

**Description:** The problem states the model should return a tensor of shape `(n,)`, but the model returns shape `(n, 1)` because `W2` has shape `(hidden_dim, output_dim)` where `output_dim=1`. The solution uses `.squeeze()` in the MSE function to handle this inconsistency.

**Why problematic:**
- The instructions say "return a tensor of shape `(n,)`" but this is impossible with the given architecture without explicitly squeezing
- Students may be confused about whether to squeeze in the model or in the loss function
- The hidden test only checks `shape[0]` rather than the full shape, masking this issue

**Suggested fix:** Either update the instructions to say the model returns shape `(n, 1)` and handle it in MSE, or explicitly instruct students to squeeze the output in the model function.

---

### Moderate Issues

#### 1. Missing Random Seed in Problem 2b
**Location:** Cell cell-20

**Description:** Problem 2b asks students to initialize weights with random values but does not set a random seed. This makes the hidden tests for checking values in `[0, 1]` potentially fragile and makes debugging harder for students.

**Suggested fix:** Add `torch.manual_seed(...)` before the solution cell or acknowledge that random initialization will vary.

#### 2. Overwriting Variable Names in Problem 3a
**Location:** Cell cell-36

**Description:** The solution overwrites `digit_images` and `digit_labels` from numpy arrays to torch tensors. This means if a student runs the cell multiple times, or runs cells out of order, they will get errors because the conversion is already done.

**Suggested fix:** Use different variable names like `digit_images_tensor` and `digit_labels_tensor`, or document that this cell should only be run once.

#### 3. Missing Documentation Links
**Location:** Throughout assignment

**Description:** The assignment uses several PyTorch concepts (autograd, DataLoader, nn.Sequential, optim.SGD, CrossEntropyLoss) without linking to official documentation.

**Suggested fix:** Add links to relevant PyTorch documentation:
- https://pytorch.org/docs/stable/autograd.html
- https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader
- https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html

#### 4. Ambiguous "Average Loss" in Problem 3d
**Location:** Cell cell-46

**Description:** The problem asks students to compute "average loss over the training data" but the solution computes `epoch_training_loss / len(train_dataloader)`, which is the average loss per batch, not per sample. These are different unless all batches have the same size.

**Suggested fix:** Clarify whether "average loss" means per-sample or per-batch, and be consistent with the mathematical definition.

#### 5. Hidden Test Potentially Gives Away Solution (Problem 1c)
**Location:** Cell cell-11

**Description:** The hidden test `assert abs(w_norm[1].item() + 0.8) < 0.2` reveals that the normalized weight w1 should be approximately -0.8. Combined with the visible verification cell that shows `w_true = torch.tensor([0.0, -4.0, 3.0])`, this could give away the expected answer structure.

**Suggested fix:** Make the tolerance in hidden tests tighter (e.g., 0.15) and remove or relocate the verification cell with `w_true`.

#### 6. Implicit Type Conversion in Problem 3a
**Location:** Cell cell-32 and cell-36

**Description:** `digit_labels` is loaded from sklearn as numpy and then accessed with `torch.unique(digit_labels)` in cell-32 (which will fail), then converted properly in cell-36.

**Suggested fix:** The cell-32 code should use `np.unique` instead of `torch.unique`, or convert to tensor first.

---

### Minor Issues

- **Problem 1a:** The hint about `y -> 2y-1` transformation uses a different form than what's needed. The actual transformation in the solution is `2 * (condition).int() - 1` which produces 1 when true and -1 when false. This is slightly confusing.

- **Problem 2d:** The variable `num_samples` is computed but could be reused more cleanly. Also, the last batch (if `num_samples` is not divisible by `batch_size`) is dropped silently.

- **Problem 3b:** The question "How many total parameters are there in the model?" appears at the end of the problem description but there's no explicit instruction to answer it (just a code cell computing it).

- **Test cell formatting:** Several test cells don't follow the exact format specified in CLAUDE.md. For example, cell-8 has the assert statements before the hidden tests section but the first line should be `# Test assertions`.

- **Problem 2c:** The hint says `torch.nn.ReLU()` but this creates a module instance. It would be cleaner to use `torch.relu` (the functional version) or `torch.nn.functional.relu`.

---

### Strengths

1. **Well-structured progression:** The assignment builds from simple (SVM with manual gradient descent) to complex (deep networks with DataLoader and nn.Sequential), providing excellent scaffolding.

2. **Good coverage of PyTorch fundamentals:** Students learn both low-level operations (manual gradient descent with autograd) and high-level abstractions (nn.Sequential, DataLoader, optim).

3. **Real datasets:** Using California Housing and Digits datasets provides realistic context and helps students understand practical data preprocessing.

4. **Clear mathematical notation:** The SVM hinge loss and labeling rule are presented with proper LaTeX notation.

5. **Helpful hints:** Most problems include useful hints that guide students without giving away the solution.

6. **Comprehensive hidden tests:** The hidden tests check for common mistakes like wrong dtypes, missing requires_grad, and incorrect value ranges.

---

### Recommendations

1. **Fix the model function design (Critical):** Either refactor Problem 2 to use a class-based approach or pass weights as parameters to the model function. This will improve testability and teach better design patterns.

2. **Clarify output shape requirements (Critical):** Be explicit about whether the model should output `(n,)` or `(n, 1)` and update the instructions accordingly.

3. **Add documentation links:** Include links to PyTorch documentation for key concepts (autograd, DataLoader, nn.Module) to help students learn to read official documentation.
---
