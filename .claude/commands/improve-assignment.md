# Improve Assignment

You are reviewing, improving, and solving a course assignment (typically a Jupyter notebook). Your goal is to make the assignment clearer, more pedagogically sound, professionally formatted, and fully solved with passing tests.

## Required Argument

The user must provide a file path to the assignment: `/improve-assignment <filepath>`

## Review Process

### 1. Read the Assignment
First, read the entire assignment file to understand its structure and content.

### 2. Check for Ambiguities
Review each problem/question for:
- **Unclear requirements**: Are the expected inputs/outputs well-defined?
- **Ambiguous phrasing**: Could a student reasonably interpret this multiple ways?
- **Missing edge cases**: Are boundary conditions specified when relevant?
- **Indexing ambiguity**: If indices are used, is it clear whether they're 0-based or 1-based?
- **Unclear data types**: Are expected types (int, float, list, tensor, etc.) specified?

### 3. Check Pedagogical Quality
Review for good teaching practices:
- **Appropriate hints**: Are hints helpful without giving away the solution?
- **Worked examples**: Complex algorithmic problems MUST include a worked example showing step-by-step reasoning
- **Progressive difficulty**: Do problems build on each other sensibly?
- **Clear learning objectives**: Is it clear what skill each problem tests?
- **Scaffolding**: Are harder problems broken into manageable steps?
- **Educational resource links**: Include links to relevant documentation (e.g., Py4E chapters, PyTorch docs, official library documentation)

### 4. Check Writing Quality
- **Grammar and spelling**: Fix any errors. The grammar should be perfect.
- **Consistent terminology**: Use the same terms throughout
- **Clear, concise language**: Avoid unnecessarily complex phrasing
- **Proper formatting**: Headers, code blocks, math notation used correctly
- **Flow**: Text should read easily and sound polished.

### 5. Check Variable Naming
- **No single-letter variables**: Rename `t`, `f`, `x`, etc. to descriptive names like `my_true`, `my_false`, `count`
- **Avoid ambiguous names**: Variables should clearly indicate their purpose
- **Exception**: Loop indices (`i`, `j`, `k`) and math conventions (`x`, `y` for coordinates) are acceptable

### 6. Fix Heading Hierarchy and Organization
- **Remove overly broad headings**: Headings like "Basics of Python" that are too vague to be useful should be removed, with their content promoted up a level
- **Proper nesting**: Each heading level should be meaningfully more specific than its parent
- **Logical grouping**: Content should be under the section it belongs to (e.g., "Conditionals" is not a "Basic data type", "Functions" and "Classes" are not "Container Data Types")
- **Problem placement**:
  - Problems testing a single topic should nest under that topic
  - Problems testing multiple topics should be at a higher level (e.g., under the parent section)
- **Descriptive section names**: Rename generic sections for clarity (e.g., "Containers" → "Container Data Types")
- **Outline should be useful**: Check the document outline—each heading should help students navigate to specific content

### 7. Ensure Consistent Formatting
- **Consistent header levels**: Use proper markdown hierarchy
- **Problem headers**: Use `### Problem N: Title` or `#### Problem N: Title` (no bold, no point values)
- **Assignment title**: `# DATASCI 315, [Assignment Type] [N]: [Topic]`
- **Sub-parts**: Format as (a), (b), (c) with clear separation
- **Consistent hint format**: Use `**Hint:**` consistently
- **Consistent expected output format**: Use `**Expected output:**` consistently
- **No trailing whitespace**: Clean up any extra spaces
- **Remove existing bold/point values**: Strip `**` and `(X pts)` from problem headers

### 8. Check Test Cases
For each problem that has test cases:
- **Minimum 2 assertions**: Each problem should have at least 2 test cases
- **Edge cases covered**: Tests should include boundary conditions
- **Clear error messages**: Assert messages should explain what's being tested
- **Correct expected values**: Verify the expected values in assertions are correct

### 9. Add Hidden Tests for Autograding
For each problem, add hidden test sections for autograding:
- **Place hidden tests AFTER visible tests** in the same cell
- **Use markers**: `# BEGIN HIDDEN TESTS` and `# END HIDDEN TESTS`
- **Cover edge cases** not shown to students
- **Include 2-4 hidden tests** per problem
- **Test different inputs** than visible tests to prevent hardcoding

### 10. Standardize Test Cell Structure
Each test cell should follow this pattern:
1. **First line must be**: `# Test assertions` (required by autograder)
2. Visible assertions with descriptive error messages
3. Print success message: `print("All tests passed!")`
4. Hidden tests section (after the print statement)

**Important**: Test cells must be SEPARATE from solution cells. Never put asserts in the same cell as `# BEGIN SOLUTION`.

Example:
```python
# Test assertions
assert result == expected, f"Expected {expected}, got {result}"
assert other_condition, "Descriptive error message"
print("All tests passed!")

# BEGIN HIDDEN TESTS
assert edge_case_result == expected, "Edge case description"
assert another_test, "Another test description"
# END HIDDEN TESTS
```

### 11. Solve All Problems
For each problem with a placeholder solution (e.g., `# your code here` or `pass`):
- **Write a complete solution**
- **Demarcate code solutions** with comments:
  ```python
  def function_name(args):
      # BEGIN SOLUTION
      # ... your solution code ...
      # END SOLUTION
  ```
- **For inline solutions** (single variable assignments): `variable = value  # SOLUTION`
- **For free-response (markdown) solutions** use blockquote-style markers:
  ```markdown
  > BEGIN SOLUTION

  Your answer text here.

  > END SOLUTION
  ```
  Note: Two newlines after `> BEGIN SOLUTION` so it renders on its own line.
- **Use best practices**: Write clean, efficient, idiomatic code
- **Add brief comments**: Explain the strategy at the start of each solution

### 12. Verify All Tests Pass
After solving all problems:
- **Run each test cell** to verify solutions are correct
- **Fix any failing tests**: Debug and correct solutions as needed
- **Ensure all assertions pass**: Every `assert` statement must succeed

### 13. Run Ruff
Ensure code quality:
- **Run `uv run ruff check <file>`**: Fix any linting issues
- **Run `uv run ruff format <file>`**: Ensure consistent formatting
- **Verify clean output**: Both commands should pass with no errors

### 14. Run Structure Validation
Run the release tool to validate notebook structure for autograding:
```bash
uv run python make_student_version.py check <file>
```

This validates that each problem has the correct otter-grader style structure:
1. **Prompt cell** (markdown) - contains "Problem N: Title"
2. **Solution cell** (code) - contains `# BEGIN SOLUTION` markers, NO asserts
3. **Test cell** (code) - contains asserts and hidden tests, NO solution markers

**Fix any reported issues:**
- **"Solution cell contains assert statements"**: Move asserts to a separate test cell after the solution
- **"Test cell contains solution markers"**: Move solution code to a separate cell before tests
- **"Test cell missing visible tests"**: Add visible assert statements before hidden tests
- **"Test cell missing hidden tests"**: Add `# BEGIN HIDDEN TESTS` section
- **"Test cell must start with '# Test assertions'"**: Add `# Test assertions` as the first line
- **"Test cell should be followed by markdown"**: Add explanatory markdown or move to correct position

**Cell separation rule**: Solution code and test assertions must be in SEPARATE cells. If a cell has both `# BEGIN SOLUTION` and `assert`, split it into two cells.

## Output Format

After completing all steps, provide:

1. **Summary of improvements made** (grouped by category)
2. **Any ambiguities or issues flagged** for instructor review
3. **Confirmation that all tests pass**
4. **Confirmation that ruff checks pass**
5. **Confirmation that structure validation passes** (`make_student_version.py check`)

## Important Guidelines

- **Demarcate solutions clearly**: Use `# BEGIN SOLUTION` / `# END SOLUTION` for code, `> BEGIN SOLUTION` / `> END SOLUTION` for markdown free-response (or `# SOLUTION` inline for single lines)
- **Don't add emoji**: Unless explicitly requested
- **Don't over-engineer**: Keep solutions simple and educational
- **Preserve problem intent**: Don't change what a problem is testing
- **Use library idioms**: Prefer torch operations over loops for tensor problems, etc.
- **Avoid deprecated patterns**: Use modern Python/library practices
- **No `isinstance` checks**: Avoid type checking in solutions
