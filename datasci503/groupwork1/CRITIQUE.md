---
## Critique: DATASCI 503, Group Work 1: Introduction to Python

### Summary
- **Critical issues**: 2
- **Moderate issues**: 8
- **Minor issues**: 6

### Critical Issues

#### 1. Test Cell Gives Away Solution (Problem 11)
**Location:** Cell 99 (Test assertions for Problem 11)

**Description:** The visible test assertions include `correct_answer`, a hardcoded 5x5 array containing the exact expected output values. Students can simply copy this array as their solution instead of generating it programmatically.

**Why problematic:** This completely undermines the learning objective of understanding random number generation and seeding. Students can pass the test without learning anything.

**Suggested fix:** Move the `correct_answer` array and the comparison assertion into the `# BEGIN HIDDEN TESTS` section. Replace with a visible test that only checks properties:
```python
# Test assertions
assert random_array.shape == (5, 5), "Array should be 5x5"
assert random_array.min() >= 0, "All values should be >= 0"
assert random_array.max() <= 1, "All values should be <= 1"
print("All tests passed!")

# BEGIN HIDDEN TESTS
correct_answer = np.array([...])
assert np.sum(np.abs(random_array - correct_answer)) < 1e-7, "Array values don't match expected"
# END HIDDEN TESTS
```

#### 2. Test Cell Gives Away Solution (Problem 12)
**Location:** Cell 102 (Test assertions for Problem 12)

**Description:** The visible test assertions include three complete `correct_mask` arrays with all expected values. Students can copy these directly as their solutions.

**Why problematic:** Same issue as Problem 11. Students can bypass the entire masking learning objective by copying the expected outputs.

**Suggested fix:** Move all `correct_mask` arrays into the hidden tests section. Replace visible tests with property checks:
```python
# Test assertions
assert masked_array1.shape == (5, 5), "masked_array1 should be 5x5"
assert masked_array2.shape == (5, 5), "masked_array2 should be 5x5"
assert masked_array3.shape == (5, 5), "masked_array3 should be 5x5"
print("All tests passed!")

# BEGIN HIDDEN TESTS
correct_mask1 = np.array([...])
# ... rest of comparison assertions
# END HIDDEN TESTS
```

### Moderate Issues

#### 1. Weak Tests for Problem 4 (Student Testing)
**Location:** Cells 76-77

**Description:** Problem 4 asks students to write their own tests, but the solution cell creates a `student_tests_passed` variable that is never actually validated. The test cell below (cell 77) re-tests `is_power_of_2` but does not verify that students wrote meaningful test expressions.

**Suggestion:** Either remove the `student_tests_passed` variable approach and just have students write direct assertions, or add tests that verify the student's test coverage (e.g., checking that certain expressions were evaluated).

#### 2. Missing Column Name Clarification (Problem 7)
**Location:** Cell 84

**Description:** The problem references "Sepal length" and "Petal width" but the actual column names are "sepal length (cm)" and "petal width (cm)". Students may waste time figuring out the exact column names.

**Suggestion:** Either use the exact column names in the problem description or add a hint: "Hint: Column names include units, e.g., 'sepal length (cm)'."

#### 3. Inconsistent Problem Numbering Style
**Location:** Cells 82-83 (Problem 6)

**Description:** Problem 6 is a free-response question but lacks a proper problem header format. It uses "### Problem 6: Summary Table Observations" but the question text is minimal and lacks context about what a complete answer should include.

**Suggestion:** Expand the problem to specify what aspects students should comment on (e.g., "Which columns are included? Which are excluded? Why might this be?").

#### 4. Ambiguous Requirements in Problem 8
**Location:** Cells 87-89

**Description:** Problem 8 asks students to "write boolean expressions to verify" but the solution uses a list of expressions stored in `verification_results`. It is unclear whether students should just write expressions that evaluate to True, or store them in a specific variable.

**Suggestion:** Make the expected format explicit: "Store your verification as a list of boolean expressions in a variable called `verification_results`, then check that all are True."

#### 5. Missing Type Hints Consistency
**Location:** Various cells

**Description:** Some function signatures include type hints (e.g., `is_power_of_2(number: int) -> bool`, `box_filter(image: np.ndarray) -> np.ndarray`) while others do not (e.g., `get_gross_pay(hours_worked, rate_per_hour)`).

**Suggestion:** For consistency and to reinforce good practices, either add type hints to all function signatures or remove them entirely.

#### 6. Test for Problem 13 Gives Away Solution
**Location:** Cell 105

**Description:** The `correct_answer` array for Problem 13 is visible in the test cell. While this is less severe than Problems 11-12 (the task is straightforward), it still allows students to bypass the learning.

**Suggestion:** Move the explicit `correct_answer` array to hidden tests and use property-based visible tests.

#### 7. Problem 15 RGB Test is Weak
**Location:** Cell 116

**Description:** The hidden tests check `np.max(diff_image) > 0` (blurring changes some pixels) and `np.min(diff_image) == 0` (some pixels unchanged). The second assertion is incorrect - blurring typically changes all pixels. Also, there is no verification that the function correctly applies the box filter to each channel.

**Suggestion:** Add more rigorous hidden tests that verify the filter is correctly applied to a small test RGB image with known expected output.

#### 8. No Hint About Integer Division for Problem 14
**Location:** Cell 106

**Description:** The problem states to compute "the floor of the average" but does not hint that Python's `//` operator performs floor division. Students unfamiliar with this operator may struggle or use `np.floor(total / count)` unnecessarily.

**Suggestion:** Add a hint: "Hint: Python's `//` operator performs integer (floor) division."

### Minor Issues

- **Cell 2:** The link to towardsdatascience.com may be behind a paywall for some students. Consider linking to a free Markdown tutorial instead.

- **Cell 12:** Multiple array creations on separate lines without storing them in variables or printing them. Only the last one is displayed. Consider adding print statements or explanatory comments.

- **Cell 39:** Two calls (`abs(arr)` and `np.absolute(arr)`) on separate lines - only the second result is displayed. Add print statements or explain this is intentional.

- **Cell 67 (Problem 2):** The phrase "Include your answer in the markdown cell below" could be clearer. Consider: "Answer this question in the markdown cell that follows the test cell."

- **Cell 70:** The free-response solution format has inconsistent spacing. The `> END SOLUTION` should have a blank line before it for consistency with other free-response problems.

- **Cells 45-46:** Two lines of code demonstrating `sum()` vs `np.sum()` and `min()`/`max()` vs `np.min()`/`np.max()` would benefit from a brief comment explaining the performance difference.

### Strengths

1. **Comprehensive Introduction:** The assignment provides an excellent scaffolded introduction to Python, NumPy, and pandas, starting with basic concepts and building to more complex operations.

2. **Good Use of Worked Examples:** Problem 14 includes a detailed worked example with matrix transformation that clearly illustrates the expected behavior.

3. **Progressive Difficulty:** Problems are well-ordered, moving from simple function writing to dataset manipulation to array operations.

4. **Helpful Hints:** Most problems include hints that guide students without giving away the solution (e.g., Problem 3's hint about repeatedly dividing).

5. **Real-World Application:** The image processing problems (13-15) connect abstract array operations to practical machine learning applications.

6. **Good Documentation Links:** The "Where to Go for Help" section provides excellent resources for self-directed learning.

7. **Clear Solution Markers:** All solution cells properly use `# BEGIN SOLUTION` / `# END SOLUTION` markers.

8. **Consistent Test Cell Format:** All test cells follow the required format with `# Test assertions` first line, visible assertions, success message, and hidden tests section.

### Recommendations

1. **Priority 1:** Fix the solution giveaway issues in Problems 11, 12, and 13 by moving exact expected values to hidden tests. This is critical for maintaining assignment integrity.

2. **Priority 2:** Add exact column names to Problem 7's description or provide a hint about the naming convention (including units in parentheses).

3. **Priority 3:** Strengthen the test for Problem 15's RGB box filter with a small test case that verifies correct per-channel filtering behavior.
---
