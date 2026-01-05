---
## Critique: Group Work 5 - Galaxy Count Prediction with Neural Networks

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

#### 1. Training Loop Gradient Zeroing Order is Unconventional
**Location:** Cell 21 (Problem 2 solution)

**Description:** The solution places `optimizer.zero_grad()` after `optimizer.step()` rather than before `loss.backward()`. While this technically works, it is unconventional and differs from the standard pattern shown in PyTorch tutorials and documentation.

**Why problematic:** Students learning from this solution may develop non-standard habits. The more typical and clearer pattern is:
```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

**Suggested fix:** Reorder to the conventional pattern in the solution:
```python
optimizer.zero_grad()
predictions = model(batch_images)
loss = loss_fn(predictions, batch_labels.long())
loss.backward()
optimizer.step()
```

#### 2. Hidden Test is Weaker Than Visible Test
**Location:** Cell 36 (final tests)

**Description:** The visible test requires `test_accuracy >= 0.60` but the hidden test only requires `test_accuracy >= 0.55`. This means a student could fail the visible test but pass the hidden test, which is backwards.

**Why problematic:** Hidden tests should catch edge cases or be stricter than visible tests, not more lenient. This defeats the purpose of hidden testing and may confuse grading.

**Suggested fix:** Either:
- Remove the redundant hidden test, or
- Make the hidden test stricter (e.g., `>= 0.60` or `>= 0.65`)

### Moderate Issues

#### 1. Placeholder Hidden Test in Problem 2
**Location:** Cell 22

**Description:** The hidden test section contains only `assert True  # Placeholder hidden test`, which provides no actual validation of the training function.

**Suggestion:** Add meaningful hidden tests such as:
- Verify the function returns two lists of the expected length
- Check that losses are decreasing (model is learning)
- Test with a minimal model to ensure the function works correctly

#### 2. Missing Loss Function Specification in Problem 2
**Location:** Cell 20 (Problem 2 instructions)

**Description:** The instructions mention using `loss_fn` but never define what loss function should be used or why cross-entropy is appropriate for multi-class classification.

**Suggestion:** Add a note explaining that `nn.CrossEntropyLoss()` should be used because this is a multi-class classification problem, and briefly explain why (combines log-softmax and negative log-likelihood).

#### 3. Escaped Characters in Test Output Messages
**Location:** Cells 16, 22, 36

**Description:** Print statements contain escaped backslashes before exclamation marks (e.g., `print(r"All tests passed\!")`). This will print the literal backslash character in the output.

**Suggestion:** Remove the raw string prefix and backslashes, or simply remove the exclamation marks:
```python
print("All tests passed!")
```

#### 4. No Guidance on Expected Training Time
**Location:** Throughout training section

**Description:** Students are not given any indication of how long training might take with the suggested hyperparameters, which could cause confusion about whether the model is stuck or working.

**Suggestion:** Add a note like "Training 100 epochs typically takes 1-2 minutes on a CPU" or add progress printing to the training loop.

#### 5. Problem 2 Has Two Separate Coding Tasks
**Location:** Cells 21 and 24

**Description:** Problem 2 asks students to implement the training loop, but then separately asks them to pick learning rate and batch size in cell 24 (also marked as SOLUTION). These are related but distinct tasks that could be confusing.

**Suggestion:** Either combine into a single problem or explicitly split into Problem 2a (implement train function) and Problem 2b (select hyperparameters).

### Minor Issues

- **Cell 9:** `torch.randint(0, len(train_images))` is missing the `size` argument and will fail. Should be `torch.randint(0, len(train_images), (1,)).item()` or use `torch.randint(len(train_images), ()).item()`.

- **Cell 10:** Same issue with `torch.randint()` as Cell 9.

- **Cell 21:** The variable `_epoch` uses underscore prefix but is never printed or used for progress tracking, which would be helpful for long training runs.

- **Cell 12:** States counts range from 0 to 6, but this is not verified or explained how this was determined from the dataset.

- **Cell 36:** The assertion error message suggests adjusting "model architecture or hyperparameters" but the visible test uses escaped characters that will display incorrectly.

- **Problem headers:** Problems are numbered 1 and 2, but Problem 2 is really about hyperparameters, so the goal-based testing section feels like an implicit "Problem 3" without a header.

### Strengths

1. **Clear learning objective:** The assignment has a well-defined goal (60% test accuracy) that students must achieve through experimentation.

2. **Good scaffolding:** The assignment provides helpful starter code (data loading, visualization, accuracy computation) so students can focus on the neural network concepts.

3. **Encourages experimentation:** The iterative nature of the assignment (try, evaluate, revise) mirrors real ML workflows and teaches important debugging skills.

4. **Appropriate difficulty:** The target accuracy of 60% on a 7-class problem is achievable but requires some effort and thought about architecture.

5. **Useful helper function:** The `reset_model_parameters()` function is a thoughtful addition that makes experimentation easier.

6. **Good hints:** Problem 1 provides concrete starting points (1-3 hidden layers, 128-512 neurons) without giving away the solution.

### Recommendations

**Top 3 priority fixes:**

1. **Fix the torch.randint() calls in cells 9 and 10** - These will cause runtime errors and prevent students from viewing the data.

2. **Fix the hidden test inconsistency in cell 36** - The hidden test should not be weaker than the visible test.

3. **Add meaningful hidden tests to Problem 2** - The placeholder hidden test provides no value for autograding the training function implementation.
---
