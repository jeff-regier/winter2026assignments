---
## Critique: Homework 2 - Practice with Python and PyTorch Tensors

### Summary
- **Critical issues**: 1
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

**1. Visible Test Reveals Answer for Problem 1**
- **Location**: Cell 6 (Problem 1 test cell)
- **Description**: The visible assertion `assert result == 906609` directly reveals the expected answer to the students before they attempt the problem.
- **Why problematic**: Students can simply hardcode `return 906609` in their function to pass all tests without implementing the algorithm. This completely undermines the pedagogical value of the problem.
- **Suggested fix**: Remove the explicit answer from visible tests. Use verification-based tests instead:
  ```python
  # Test assertions
  result = three_digit_palindrome()
  print(f"Largest palindrome from 3-digit products: {result}")

  # Verify it's actually a palindrome
  assert str(result) == str(result)[::-1], "Result should be a palindrome"

  # Verify it can be factored into two 3-digit numbers
  found_factors = False
  for i in range(100, 1000):
      if result % i == 0:
          other = result // i
          if 100 <= other <= 999:
              found_factors = True
              break
  assert found_factors, "Result should be product of two 3-digit numbers"

  # Verify it's the largest (check that no larger palindrome exists)
  assert result > 900000, "Result should be a large palindrome"

  print("All tests passed!")
  ```
  Move the exact value check to hidden tests only.

### Moderate Issues

**1. Visible Test Reveals Answer for Problem 2**
- **Location**: Cell 9 (Problem 2 test cell)
- **Description**: The visible assertion `assert nfib(1000) == 4782` reveals a specific answer that students could hardcode.
- **Suggestion**: Move specific large-input tests to hidden tests. Keep visible tests focused on small, verifiable cases like `nfib(1)`, `nfib(2)`, `nfib(3)` where students can manually verify correctness.

**2. Problem 3 Missing Error Messages on Initial Assertions**
- **Location**: Cell 12 (Problem 3 test cell)
- **Description**: The first six assertions lack descriptive error messages:
  ```python
  assert is_stackable([7, 5, 3, 6, 10])
  assert not is_stackable([2, 5, 6, 3])
  ```
- **Suggestion**: Add error messages to all assertions for better debugging feedback:
  ```python
  assert is_stackable([7, 5, 3, 6, 10]), "Array [7, 5, 3, 6, 10] should be stackable"
  assert not is_stackable([2, 5, 6, 3]), "Array [2, 5, 6, 3] should not be stackable"
  ```

**3. Inconsistent Success Message Format**
- **Location**: Cells 21, 24, 27, 30, 33 (Problems 4-8 test cells)
- **Description**: Problems 4-8 print "Assertions passed!" while Problems 1-3 print "All tests passed!" as specified in CLAUDE.md conventions.
- **Suggestion**: Standardize all test cells to use `print("All tests passed!")` for consistency.

**4. Problem 7 Cropping Specification Ambiguity**
- **Location**: Cell 28 (Problem 7 description)
- **Description**: The phrase "rows 100-200 and columns 100-400 (using 0-based indexing, inclusive on both ends)" could be clearer. Students may be confused whether "inclusive on both ends" applies to both the row and column ranges or just one.
- **Suggestion**: Rephrase more explicitly: "Crop the image to include rows 100 through 200 (inclusive) and columns 100 through 400 (inclusive), using 0-based indexing. The result should have dimensions 101 x 301 x 3."

**5. Problem 8 Missing Link to Documentation**
- **Location**: Cell 31 (Problem 8 description)
- **Description**: The hint mentions `Tensor.unfold()` for the advanced approach but provides no documentation link. This is an advanced PyTorch operation that students may not have encountered.
- **Suggestion**: Add a link to the PyTorch documentation:
  ```markdown
  **Vectorized approach (advanced):** Use [`Tensor.unfold()`](https://pytorch.org/docs/stable/generated/torch.Tensor.unfold.html) to extract all 11x11 windows at once...
  ```

**6. No Documentation Links in Part 2 Introduction**
- **Location**: Cell 13 (Part 2 intro)
- **Description**: While the assignment links to external resources for Part 1 (Project Euler, LeetCode), Part 2 mentions PyTorch tensors without linking to the PyTorch documentation.
- **Suggestion**: Add a link to PyTorch tensor documentation:
  ```markdown
  ...using PyTorch's tensor operations. See the [PyTorch Tensor documentation](https://pytorch.org/docs/stable/tensors.html) for a complete reference.
  ```

### Minor Issues

- **Problem 4 test cell (Cell 21)**: The comment says `# verify only blue channel has values` but does not check that the blue channel is specifically non-zero in all pixels, only that the sum is non-zero. This is technically correct but could be misleading.

- **Problem 6 hint complexity**: The hint for vertical flip is quite detailed and almost gives away the solution. Consider simplifying to: "Use tensor indexing with a reversed index tensor created via `torch.arange`."

- **Test cell in Problem 2 (Cell 9)**: The helper function `get_fib(k)` is defined inside the test cell. While functional, this adds complexity to the test cell. Consider moving verification logic to hidden tests.

- **Problem 5 description**: The channel ordering (blue=0, red=1, green=2 for column position) differs from the standard RGB ordering (red=0, green=1, blue=2 for array index). While this is intentional for visual effect, it could be confusing. Consider adding a clarifying note.

- **Variable naming in Problem 8 solution**: Uses `h, w, c` which are single-letter-ish variable names. While common in image processing, the CLAUDE.md guidelines prefer descriptive names except for loop indices.

### Strengths

1. **Excellent progression**: The assignment smoothly transitions from pure Python algorithmic problems (Part 1) to PyTorch tensor operations (Part 2), building complexity gradually.

2. **Good worked examples**: Problem 3 includes a detailed step-by-step worked example showing why `[7, 5, 3, 6, 10]` is stackable and why `[2, 5, 6, 3]` is not.

3. **Helpful hints**: Each problem includes a hint that guides students toward the solution without giving it away entirely (with the exception of Problem 6 which is overly detailed).

4. **Comprehensive test coverage**: The visible tests check multiple aspects of correctness (shape, values, edge cases), and hidden tests add additional verification.

5. **Clear problem statements**: Most problems are well-written with clear requirements and expected outputs.

6. **Good use of visual feedback**: Image manipulation problems display results, helping students verify their work visually.

7. **Multiple solution approaches offered**: Problem 8 explicitly describes both a loop-based and vectorized approach, accommodating different skill levels.

8. **External resource links**: Part 1 appropriately links to Project Euler, LeetCode, and the digital images introduction page.

### Recommendations

1. **High Priority**: Fix the visible test in Problem 1 that reveals the answer (906609). This is the most critical issue as it allows students to bypass the problem entirely.

2. **Medium Priority**: Add descriptive error messages to all assertions in Problem 3, and standardize the success message to "All tests passed!" across all problems for consistency.

3. **Medium Priority**: Add PyTorch documentation links in Part 2, especially for the advanced `Tensor.unfold()` method mentioned in Problem 8.
---
