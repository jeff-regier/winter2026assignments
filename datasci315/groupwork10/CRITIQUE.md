---
## Critique: Group Work 10 - Transformers

### Summary
- **Critical issues**: 1
- **Moderate issues**: 5
- **Minor issues**: 4

### Critical Issues

#### 1. Inconsistent Alias Usage for torch.nn.functional
**Location**: Cell 2 (imports) and throughout the assignment

**Description**: The import statement uses `from torch.nn import functional` but the hints and conventional PyTorch usage refer to `F.softmax`. This creates confusion between what students should use.

**Why Problematic**: In Problem 1's hint, students are told to use `F.softmax`, but `F` is never imported. The solution uses `functional.softmax` which is inconsistent with PyTorch conventions and the hint. Students will get `NameError: name 'F' is not defined` if they follow the hint literally.

**Suggested Fix**: Either:
- Change the import to `from torch.nn import functional as F` and update all references to `F.softmax`, `F.log_softmax`, OR
- Update the hint in Problem 1 to say "Use `functional.softmax` with `dim=-1`"

### Moderate Issues

#### 1. Missing Input Validation Guidance for Positional Encoding
**Location**: Problem 4 (Cell 14-15)

**Description**: The problem states `embed_dim` must be even but doesn't guide students on how to handle this or whether to validate it.

**Suggestion**: Either add an assertion at the start of the function template to enforce even dimensions, or note in the problem description that students don't need to validate this assumption.

#### 2. Worked Example Uses Approximate Values Without Explanation
**Location**: Problem 1 (Cell 4)

**Description**: The worked example shows `Attention weights = [[0.67, 0.33], [0.33, 0.67]]` without showing the softmax calculation. Students might not understand where these numbers come from.

**Suggestion**: Add the softmax calculation step: "softmax([0.707, 0]) = [exp(0.707)/(exp(0.707)+exp(0)), exp(0)/(exp(0.707)+exp(0))] = [0.67, 0.33]"

#### 3. Problem 5 Mask Conversion Could Be Clearer
**Location**: Problem 5 (Cell 18)

**Description**: The instructions mention using `torch.where` to convert the boolean mask but don't provide enough context about why this is needed or a concrete example. The solution also creates new tensors without specifying device, which could cause issues.

**Suggestion**: Add a brief code snippet showing the conversion:
```python
# Convert boolean mask to float mask
# bool_mask: True where to mask
# float_mask = torch.where(bool_mask, torch.tensor(-inf), torch.tensor(0.0))
```

#### 4. Test Range for Perplexity Is Too Wide
**Location**: Problem 6 (Cell 23)

**Description**: The assertion `perplexity > 50 and perplexity < 200` is a very wide range that might pass incorrect implementations. For a random model with vocab_size=100, the expected perplexity should be closer to 100.

**Suggestion**: Tighten the range to something like `75 < perplexity < 125` or provide a more principled bound based on the random initialization.

#### 5. Problem 3 Lacks Sufficient Scaffolding
**Location**: Problem 3 (Cell 10-11)

**Description**: The problem asks students to "set `causal_attention_weights`" but provides minimal guidance. Students need to understand they should call both `create_causal_mask` and `scaled_dot_product_attention`.

**Suggestion**: Add explicit steps:
1. "Create a causal mask using your `create_causal_mask` function with `test_seq_len`"
2. "Call `scaled_dot_product_attention` with the test tensors and the causal mask"
3. "Store the attention weights in `causal_attention_weights`"

### Minor Issues

- **Cell 5**: The solution uses `key.transpose(-2, -1)` but the hint recommends `torch.bmm`. While both work, the solution could use `torch.bmm(query, key.transpose(1, 2))` for consistency with the hint.

- **Problem headers**: Problem headers are formatted correctly as `### Problem N: Title`, but some could be more descriptive (e.g., "Problem 3: Verify Causal Masking Works" could be "Problem 3: Verify Causal Masking Prevents Future Attention").

- **Resources section**: The link to "The Illustrated Transformer" is excellent, but it would help to add a brief note about which sections are most relevant for each problem.

- **Cell 19**: The solution creates tensors with `torch.tensor(float("-inf"))` and `torch.tensor(0.0)` without specifying dtype or device, which could cause dtype mismatches on different hardware.

### Strengths

1. **Excellent Background Sections**: The mathematical explanations of scaled dot-product attention and positional encoding are clear and well-formatted with proper LaTeX equations.

2. **Progressive Complexity**: The assignment builds logically from basic attention to a complete transformer model, with each problem using components from previous problems.

3. **Strong Worked Example**: Problem 1 includes a detailed step-by-step worked example that shows the complete attention calculation, which is very helpful for understanding.

4. **Good Test Coverage**: The hidden tests check edge cases (seq_len=1, single sequence, diagonal attention) and verify important invariants (deterministic output, attention weight sums).

5. **Practical Hints**: The hints about using `torch.triu` and the formula for the divisor term in positional encoding are appropriately helpful without giving away the solution.

6. **Comprehensive Summary**: The final summary cell effectively recaps what students learned and connects it to real-world applications.

7. **Appropriate Resource Links**: Links to the original "Attention Is All You Need" paper, PyTorch documentation, and "The Illustrated Transformer" give students good reference material.

### Recommendations

1. **Fix the F/functional import inconsistency** (Critical): This will cause immediate errors for students who follow the hints. Either update the import to use `F` or update all hints to use `functional`.

2. **Add more scaffolding to Problem 3**: The current instructions are too sparse. Provide explicit steps and possibly a code comment template.

3. **Show the softmax calculation in the worked example**: The jump from scaled scores to attention weights is too large; showing the actual softmax calculation will help students understand the connection.
---
