---
## Critique: DATASCI 315, Homework 1: Python Tutorial

### Summary
- **Critical issues**: 1
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

#### 1. Problem 3 Test Cell Does Not Test Multiple Inputs
**Location:** Cell 66 (Test assertions for Problem 3: Palindrome Check)

**Description:** The test cell only checks that `p3_result == "Yes"` for the hardcoded input `word = "level"`. The problem asks students to write code that works for any word, but the visible and hidden tests only verify the result for this single palindrome example.

**Why problematic:** A student could hardcode `p3_result = "Yes"` and pass all tests. The tests never verify behavior for non-palindromes (e.g., "hello" should return "No") or other palindromes. This makes autograding ineffective and fails to verify students understand the concept.

**Suggested fix:** Change the problem structure to define a function `is_palindrome(word)` that returns "Yes" or "No", then test multiple cases:
```python
# Test assertions
assert is_palindrome("level") == "Yes", "level is a palindrome"
assert is_palindrome("hello") == "No", "hello is not a palindrome"
assert is_palindrome("racecar") == "Yes", "racecar is a palindrome"
assert is_palindrome("a") == "Yes", "single character is a palindrome"
```

### Moderate Issues

#### 1. Problem 1 Solution Leakage in Visible Tests
**Location:** Cell 29 (Test assertions for Problem 1)

**Description:** The visible assertions directly reveal the expected answers:
```python
assert q1 == ans1, f"q1: expected {ans1}, got {q1}"
```
Since `q1`, `q2`, etc. are computed from the expressions, students can see the expected values by looking at what the expressions evaluate to. Additionally, the assertion messages print the expected answers.

**Why problematic:** The exercise asks students to "predict" values, but they can simply run the expressions first and then fill in the answers. The assertions also print the correct answer in error messages.

**Suggested fix:** Remove the expected value from error messages or restructure so students must provide predictions before seeing the computed values:
```python
assert q1 == ans1, "Your prediction for q1 is incorrect"
```

#### 2. Problem 4 Header Inconsistency
**Location:** Cell 74

**Description:** The header uses `#### Problem 4:` (four hashes) while other problems use `### Problem N:` (three hashes).

**Why problematic:** Inconsistent formatting reduces readability and violates the convention stated in CLAUDE.md ("Use `### Problem N: Title` or `#### Problem N: Title`" - while both are allowed, consistency within an assignment is preferred).

**Suggested fix:** Change to `### Problem 4: List Comprehension with Conditions` for consistency with other problems.

#### 3. Problem 5, 6, 7 Header Inconsistency
**Location:** Cells 92, 106, 114

**Description:** Problems 5, 6, and 7 also use `#### Problem N:` (four hashes) while Problems 1, 2, 3, 8, 9, 10 use `### Problem N:` (three hashes).

**Why problematic:** Mixed header levels create visual inconsistency and potentially affect notebook navigation/outline views.

**Suggested fix:** Standardize all problem headers to use `###`.

#### 4. Missing Edge Case for Problem 8: Fibonacci
**Location:** Cell 126 (Test assertions for Problem 8)

**Description:** The tests do not check for negative input handling. A student's recursive solution will cause infinite recursion or return incorrect values for negative inputs.

**Why problematic:** Students might not consider edge cases, and the autograder cannot verify robust implementations.

**Suggested fix:** Add a note about input assumptions or add edge case handling:
```python
# In hidden tests
assert fibonacci(-1) == 0 or raises_exception  # Define expected behavior
```
Or clarify in the problem statement: "Assume n >= 0."

#### 5. Problem 9 Test Variable Name Collision
**Location:** Cell 140

**Description:** The test cell reuses the variable name `p4_result` (from Problem 4) to store withdrawal results:
```python
p4_result = account.withdraw(30)
```

**Why problematic:** This is confusing and could mask issues if students run cells out of order. It suggests copy-paste errors in test creation.

**Suggested fix:** Rename to `withdraw_result` or `success`:
```python
success = account.withdraw(30)
assert success, "Withdrawal of 30 should succeed"
```

#### 6. Long Test Cell for Problem 10
**Location:** Cell 143

**Description:** The test cell for Problem 10 is extremely long (50+ lines) and combines many test scenarios with intermediate state mutations.

**Why problematic:** Long test cells are hard to debug when failures occur. Students cannot easily identify which specific feature is failing.

**Suggested fix:** Consider breaking into multiple test cells or adding section comments to clearly delineate test scenarios.

### Minor Issues

- **Cell 12**: Link text says "Py4E Variables chapter" but Python does not have "long integers" as a separate type in Python 3 (they were unified with `int`). Consider updating or removing this mention.

- **Cell 21**: Comment says "single quotes" but the code uses double quotes. The comment and code are mismatched (both work, but the comment is inaccurate).

- **Cell 27**: Problem 1 asks students to "predict" values but there is no mechanism to verify predictions were made before running code.

- **Cell 46**: Comment says `# Prints "[0, 1, 2, 3, 4]"` but should be `# Prints [0, 1, 2, 3, 4]` (without extra quotes around the output).

- **Cell 57**: The example for `break` is somewhat contrived. The condition `a[-1] >= 18` is checking for the "last multiple of 3 before 20" but 18 is included in the output, so the comment "print multiples of 3 below 20" is accurate but the logic could be clearer.

- **Cell 64 (Problem 3)**: Could benefit from an additional example of a non-palindrome to clarify expected behavior.

- **Cell 115 (Problem 7)**: The starter code has a comment `# add more coordinates here` inside the locations dict, but the solution completely replaces the dict. This could confuse students about whether to extend or replace.

- **Cell 137**: The Py4E link uses "Objects" with capital O but other links use lowercase lesson names. Minor inconsistency.

### Strengths

1. **Comprehensive Coverage**: The assignment covers all fundamental Python concepts (types, containers, loops, functions, classes) in a logical progression.

2. **Excellent Documentation Links**: Consistent references to Py4E chapters provide students with additional resources for self-study.

3. **Good Scaffolding**: Each concept is introduced with worked examples before problems, following sound pedagogical practice.

4. **Progressive Difficulty**: Problems build in complexity from simple type coercion (Problem 1) to a full shopping cart system (Problem 10).

5. **Real-World Examples**: The BankAccount and ShoppingCart classes demonstrate practical applications of OOP concepts.

6. **Helpful Hints**: Most problems include relevant hints pointing to specific Python features students should use.

7. **Thorough Hidden Tests**: Most problems have meaningful hidden tests that check edge cases and implementation details.

8. **Clear Introduction**: The opening clearly states learning objectives and reassures students that GSIs are available to help.

9. **Good Use of Markdown**: Error cases are shown as code blocks with comments explaining the error, avoiding actual runtime errors in the notebook.

### Recommendations

**Top 3 Priority Fixes:**

1. **Fix Problem 3 Testing**: Convert to a function-based problem or add tests for non-palindrome inputs. This is the most critical issue as students could pass without understanding the concept.

2. **Standardize Problem Headers**: Change all `####` headers to `###` for consistency. A simple find-and-replace can fix this across cells 74, 92, 106, and 114.

3. **Fix Variable Name Collision in Problem 9 Tests**: Rename `p4_result` to `withdraw_result` to avoid confusion and potential issues with out-of-order cell execution.
---
