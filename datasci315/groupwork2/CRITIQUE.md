---
## Critique: Group Work 2 - Shallow Neural Networks

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

#### 1. Free-Response Problems Lack Solution Markers
**Location**: Cells 92, 94, 96 (Problem 8 text responses)

**Description**: Problem 8 asks students to predict Gaussian distribution behavior in three sub-questions, but the markdown cells for answers simply contain "(Type your answer here)" without proper solution markers (`> BEGIN SOLUTION` / `> END SOLUTION`).

**Why problematic**: The student version generator will not strip these placeholder texts, and autograding cannot distinguish between template text and student responses. The verification cell (97-98) uses a boolean `problem_8_completed = True` which is set in the solution but has no actual validation mechanism for the text answers.

**Suggested fix**: Replace the text answer cells with proper blockquote markers:
```markdown
> BEGIN SOLUTION

[Expected answer here]

> END SOLUTION
```

#### 2. Problem 8 Test Cell Has No Real Validation
**Location**: Cell 98

**Description**: The test cell only checks `assert problem_8_completed` which is a boolean set to `True` in the solution cell. This provides zero validation that students actually answered the questions.

**Why problematic**: Students could leave the text responses blank and still pass all tests if they copy the solution cell pattern.

**Suggested fix**: Either:
1. Remove the artificial boolean check and make this a pure free-response problem
2. Add proper free-response markers and document that these are manually graded

---

### Moderate Issues

#### 1. Inconsistent Training Data Between Parts
**Location**: Cells 6 and 82

**Description**: The assignment defines `x_train` and `y_train` twice with different values. Part 1 uses one dataset (cells 6), and Part 3 redefines them with different y-values (cell 82). For example, y_train[0] is -0.15934537 in Part 1 but -0.25934537 in Part 3.

**Suggestion**: Either use distinct variable names (e.g., `x_train_1`, `x_train_3`) or explicitly note that the data is intentionally different for pedagogical reasons.

#### 2. ReLU Function Defined Twice with Different Implementations
**Location**: Cells 4 and 42

**Description**: The `relu` function is defined twice with different implementations:
- Cell 4: `torch.maximum(x, torch.zeros_like(x))`
- Cell 42: `torch.clamp(preactivation, min=0.0)`

**Suggestion**: Consolidate to one implementation or explicitly note this is intentional to show equivalent approaches.

#### 3. Missing Documentation Links for Key Concepts
**Location**: Throughout, especially cells discussing loss functions and softmax

**Description**: While cell 2 links to PyTorch tensors documentation, there are no links for:
- ReLU activation
- Softmax function
- Cross-entropy loss
- The "Understanding Deep Learning" textbook mentioned in cell 15

**Suggestion**: Add documentation links where relevant, especially for the textbook figures referenced.

#### 4. Problem 2 Test Cell Checks Visible Assertions Give Away Structure
**Location**: Cell 18

**Description**: The visible tests explicitly check `model.layer1.weights.shape == (3, 1)` which tells students exactly what data structure to use, reducing the learning challenge.

**Suggestion**: Move structural checks to hidden tests, keep only behavioral checks (e.g., output shape, forward pass works) in visible tests.

#### 5. No Scaffolding for Problem 4 Cross-Entropy Loss
**Location**: Cell 32-37

**Description**: Problem 4 asks students to build a classifier and then uses the provided `binary_cross_entropy` function, but there's no task asking students to understand or compute anything with the loss. The cell 37 just runs the loss function without any assertion or discussion.

**Suggestion**: Either:
1. Add a sub-problem asking students to explain what the cross-entropy loss measures
2. Add assertions checking the loss is in a reasonable range
3. Have students predict what happens to loss as model improves

#### 6. Problem 3 Expected Loss Value May Vary
**Location**: Cell 21-22

**Description**: The problem states "it should be approximately 9.385" for the loss, but this depends on the model parameters set in Problem 2. If students make any error in Problem 2, this cascading failure will be confusing.

**Suggestion**: Add a note that the expected value assumes correct completion of Problem 2, or reset the model parameters at the start of Problem 3.

---

### Minor Issues

- **Cell 8**: The note "This is similar to `torch.nn.Linear`" could link to torch.nn.Linear documentation
- **Cell 11**: Formula uses $A_{ji}$ but earlier text uses $A$ without subscripts - consider consistent notation
- **Cell 15**: "Figure 3.4 in the Textbook" should link to or cite the textbook properly
- **Cell 24**: "Why 7 parameters?" is posed rhetorically but never answered - could add a hint
- **Cell 52-53**: "equation 4.15" reference needs textbook citation
- **Cell 66**: "Consult figure 4.6 and equations 4.15" - unclear source, needs citation
- **Cell 83**: Grammatically awkward: "Let's compute the loss. We'll compute the the least squares error" (double "the")
- **Cell 92-96**: Placeholder text should be in consistent format (currently uses parentheses)

---

### Strengths

1. **Well-structured progression**: The assignment builds logically from basic components (Linear layer, ReLU) to complete networks, then to matrix form, and finally to loss functions.

2. **Excellent hands-on learning**: Having students implement `Linear` class from scratch before using PyTorch's version is pedagogically sound.

3. **Good visual aids**: Plots are included throughout to help students visualize network behavior and training data.

4. **Practical grid search demonstration**: The "Fun Parameter Optimization Without Gradients" section effectively demonstrates why gradient-based optimization is necessary.

5. **Clear mathematical notation**: LaTeX formulas are well-formatted and aligned with code implementations.

6. **Strong test coverage**: Most problems have good visible assertions with clear error messages, plus hidden tests for autograding.

7. **Appropriate difficulty**: The problems build incrementally with reasonable complexity increases.

8. **Both regression and classification**: Good coverage of the two main supervised learning paradigms.

---

### Recommendations

**Priority 1**: Fix Problem 8 to either use proper free-response markers or remove the artificial boolean validation. This is a grading correctness issue.

**Priority 2**: Add explicit references/links to the "Understanding Deep Learning" textbook and figure numbers. Students need to be able to access these resources.

**Priority 3**: Resolve the duplicate `x_train`/`y_train` definitions either by using different variable names or adding explicit notes about the different datasets. This prevents student confusion when comparing outputs across parts.
---
