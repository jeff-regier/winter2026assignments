---
## Critique: Group Work 4 - PyTorch Training Pipeline and FashionMNIST

### Summary
- **Critical issues**: 1
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

#### 1. Problem 1 Header Inconsistency with Subproblems
**Location:** Cell 14 (Problem 1: Shapes and Parameters)

**Description:** Problem 1 has parts (a) and (b) but does not specify these as separate problems or provide clear instructions on what variables students should define. The problem asks students to "Explain your solution" but the test cell checks for specific variables (`w2_shape`, `b2_shape`, `total_params`) that are never mentioned in the problem statement.

**Why problematic:** Students will not know what variable names to use without looking at the test cell, which defeats the purpose of autograding and creates confusion.

**Suggested fix:** Explicitly state the required variable names in the problem statement:
```markdown
(a) What is the shape of $W_2$ and $b_2$? Store these as tuples in `w2_shape` and `b2_shape`.

(b) What is the total number of parameters in this model? Store this in `total_params`.
```

### Moderate Issues

#### 1. Missing Variable Name Specifications Throughout
**Location:** Problems 2a-2e (Cells 25, 28, 32, 35, 38)

**Description:** Multiple problems do not specify the expected variable names that will be tested. For example:
- Problem 2a doesn't specify `train_dataloader` and `test_dataloader`
- Problem 2b doesn't specify `flatten_layer` and `train_flat_features`
- Problem 2c doesn't specify `classification_model`
- Problem 2d doesn't specify `classification_loss_fn` and `initial_loss`
- Problem 2e doesn't specify `classification_optimizer`, `classification_train_loss`, `classification_test_loss`, `classification_test_accuracy`

**Suggestion:** Add explicit variable name requirements to each problem statement.

#### 2. Problem 2a Missing Shuffle Specification
**Location:** Cell 25

**Description:** The problem asks to create DataLoaders but doesn't specify whether to shuffle the data. The solution uses `shuffle=True` for training and `shuffle=False` for test, but students might use different settings.

**Suggestion:** Add guidance: "Shuffle the training data but not the test data."

#### 3. Test Cell Gives Away Solution Structure in Problem 2c
**Location:** Cell 34

**Description:** The test assertion `len(list(classification_model.parameters())) == 6` in the hidden tests reveals that the model should have exactly 6 parameter tensors, which gives away the architecture structure.

**Suggestion:** Move this assertion to visible tests with a more educational error message, or test the output shape and parameter count only without revealing internal structure.

#### 4. Inconsistent Problem Header Formatting
**Location:** Cells 14, 25, 28, 32, 35, 38

**Description:** Problem 1 uses `### Problem 1:` format, while Problems 2a-2e use `#### Problem 2a:` format. The inconsistency between `###` and `####` headers and the use of subproblem letters (2a, 2b, etc.) versus separate problems is confusing.

**Suggestion:** Use consistent formatting. Either make Problem 2's subproblems separate problems (Problem 2, 3, 4, 5, 6) or use consistent header levels throughout.

#### 5. Learning Objectives Mismatch
**Location:** Cell 0

**Description:** The stated learning objectives mention "Tensors in PyTorch" and "Automatic differentiation (autograd) in PyTorch" but the assignment doesn't explicitly cover tensors (beyond basic usage) or demonstrate autograd concepts directly. Students don't implement any manual gradient computation or tensor operations.

**Suggestion:** Either add introductory content covering tensors and autograd explicitly, or update the learning objectives to match the actual content (DataLoaders, Sequential models, training loops).

#### 6. Problem 2e Is Too Complex for a Single Problem
**Location:** Cell 38

**Description:** Problem 2e requires students to implement a complete training loop with multiple components: optimizer initialization, epoch loop, batch loop, forward pass, backward pass, gradient zeroing, test evaluation, and accuracy computation. This is a lot for students learning PyTorch for the first time.

**Suggestion:** Break this into multiple sub-steps or provide more scaffolding code (e.g., provide the training loop skeleton and have students fill in specific parts).

### Minor Issues

- **Cell 6:** States "there are $B=25$ batches" but this depends on the train/test split which leaves 800 samples, giving 25 batches. This could be confusing if students don't follow the math.

- **Cell 17:** References "the optimization routine we saw above for simple linear regression" but there is no linear regression example earlier in the notebook - only the synthetic data regression problem.

- **Cell 32:** The note about `CrossEntropyLoss` and softmax is helpful but could be expanded to explain what "automatically normalizes" means (i.e., applies log-softmax internally).

- **Problem 2d test cell (Cell 37):** The bounds check `initial_loss.item() < 10` is arbitrary and could fail for edge cases. A random initialization should give loss around -log(0.1) = 2.3 for 10 classes, but the bound of 10 is generous.

- **Missing documentation links:** Problems reference `nn.Flatten`, `CrossEntropyLoss`, etc. but don't provide direct links to their PyTorch documentation pages.

### Strengths

1. **Good progression:** The assignment builds from regression to classification, introducing concepts incrementally.

2. **Clear worked examples:** The regression section provides a complete worked example before asking students to apply concepts to classification.

3. **Appropriate scaffolding:** The assignment provides substantial example code and explanations before each problem.

4. **Visual feedback:** The assignment includes data visualization and loss plotting, helping students understand their results.

5. **Real dataset:** Using FashionMNIST instead of toy data makes the assignment more engaging and provides realistic training experience.

6. **Test assertions have descriptive error messages:** Each test cell includes clear error messages that will help students debug their solutions.

7. **Proper use of `torch.no_grad()`:** The examples and solutions correctly demonstrate when to use `torch.no_grad()` for evaluation.

### Recommendations

1. **Add explicit variable name requirements** to all problem statements. This is essential for autograding and reduces student confusion.

2. **Break down Problem 2e** into smaller steps or provide more scaffolding. The current problem asks students to implement too many concepts at once.

3. **Update learning objectives** to match actual content, or add explicit coverage of tensors and autograd concepts in the instructional sections.
---
