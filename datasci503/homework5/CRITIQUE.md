---
## Critique: DATASCI 503, Homework 5: Resampling Methods

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 7

### Critical Issues

#### 1. Test Assertion Gives Away Solution Value (Problem 1d)
**Location:** Cell 8

**Description:** The visible test assertion reveals the exact expected answer:
```python
assert abs(prob_in_sample_n5 - 0.6723) < 0.001, f"Expected ~0.6723, got {prob_in_sample_n5}"
```

**Why problematic:** Students can simply assign `prob_in_sample_n5 = 0.6723` without understanding the underlying formula. This defeats the pedagogical purpose of the problem and undermines autograding integrity.

**Suggested fix:** Replace with a structural test that verifies the formula was applied correctly:
```python
# Test assertions
assert isinstance(prob_in_sample_n5, float), "Result should be a float"
assert 0 < prob_in_sample_n5 < 1, "Probability must be between 0 and 1"
print("All tests passed!")
```

#### 2. Multiple Test Assertions Give Away Solution Values
**Location:** Cells 12, 16, 36, 40, 45, 54, 58, 62, 66, 70, 74, 85

**Description:** Throughout the assignment, visible test assertions reveal expected numerical values. Examples include:
- `assert abs(prob_in_sample_n100 - 0.634) < 0.01` (Cell 12)
- `assert abs(mu_hat - 22.533) < 0.01` (Cell 36)
- `assert abs(se_mu_hat - 0.409) < 0.01` (Cell 40)

**Why problematic:** This is a systemic issue that allows students to bypass the learning objectives by hardcoding expected values.

**Suggested fix:** Move numerical checks to hidden tests. Visible tests should verify type, range, or structural properties only.

### Moderate Issues

#### 1. Missing Data File Path Verification
**Location:** Cells 35, 69

**Description:** The assignment references `./data/boston.csv` and `./data/weekly.csv` without specifying whether these files will be provided or where students can obtain them.

**Suggestion:** Add a markdown cell at the beginning of the assignment that explains data file locations or provides download instructions.

#### 2. Undefined Variable in Test Cell (Problem 3c)
**Location:** Cell 30

**Description:** The test asserts `errors_df["Mean"].idxmin() == 2`, assuming the DataFrame index starts at 1. While the solution sets `errors_df.index = errors_df.index + 1`, the test relies on implementation details.

**Suggestion:** Make the test more robust by checking relative ordering rather than specific index values:
```python
assert errors_df["Mean"].idxmin() == 2, "The quadratic model should have the lowest mean error"
```

#### 3. Bootstrap Function Parameters Could Be Confusing
**Location:** Cell 43

**Description:** The `boot_se` function has an `n` parameter with default `n = n or df.shape[0]`. The parameter name shadows the global variable `n` used in earlier problems, which could cause confusion.

**Suggestion:** Rename the parameter to `sample_size` or `bootstrap_n` for clarity.

#### 4. Problem 5 Does Not Explain Boston Dataset
**Location:** Cell 34

**Description:** Problem 5 references "the Boston housing data set" without providing context about what the dataset contains, what `medv` represents, or the ethical considerations of this dataset.

**Suggestion:** Add a brief description: "The Boston housing dataset contains information about housing values and characteristics in Boston suburbs. The variable `medv` represents the median value of owner-occupied homes in $1000s." Consider also noting that this dataset has been deprecated in sklearn due to ethical concerns about its creation.

#### 5. Inconsistent Random Seed Usage
**Location:** Cells 43-44, 57, 65

**Description:** The bootstrap function uses `seed=2024` in later problems, but Problem 3(a) uses `rng = np.random.default_rng(1)`. This inconsistency could confuse students about reproducibility practices.

**Suggestion:** Use consistent seeding conventions throughout, or explain why different seeds are used.

#### 6. Missing Interpretation Guidance in Problem 3(c)
**Location:** Cell 26

**Description:** The problem asks students to compute cross-validation errors but provides minimal guidance on how to interpret or compare MSE values across models.

**Suggestion:** Add a hint about interpreting MSE values and their relative magnitudes.

### Minor Issues

- **Problem 2 has no code cell or test:** While it is correctly marked as free response, there could be a follow-up code exercise demonstrating the concept.

- **Problem 4 inconsistent formatting:** The phrase "log odds" should be "log-odds" for consistency with statistical terminology.

- **Cell 69 uses `pd.get_dummies` in a potentially confusing way:** Using `drop_first=True` creates a single column, which could be done more simply with `(weekly_df["Direction"] == "Up").astype(int)`.

- **Variable naming in Cell 29:** `errors_df` could be more descriptively named as `cv_errors_df` or `fold_errors_df`.

- **Problem 6(d) description could be clearer:** The phrase "indicate this as a 1, and otherwise indicate it as a 0" could specify storing in a list or array.

- **Missing newline after `> BEGIN SOLUTION` in Cell 71:** The free-response solution does not follow the convention of two newlines after the marker.

- **Test tolerance inconsistency:** Some tests use tolerance of 0.001, others use 0.01 or 0.02. A consistent approach would improve clarity.

### Strengths

1. **Well-structured progression:** The assignment moves logically from theoretical understanding (Problem 1) through simulation (Problem 3) to real data application (Problems 5-6), building conceptual understanding incrementally.

2. **Clear connection to course concepts:** The introduction effectively connects resampling methods to the bias-variance tradeoff, providing motivation for the techniques.

3. **Good use of scaffolding:** Problem 1 breaks down the bootstrap probability derivation into manageable steps (a-f), helping students build intuition.

4. **Balanced theory and practice:** The assignment includes both mathematical derivations (Problems 1, 4) and practical coding exercises (Problems 3, 5, 6).

5. **Appropriate use of free-response problems:** Problems 2 and 4 are correctly formatted as free-response questions with blockquote-style solution markers.

6. **Good test coverage in hidden tests:** The hidden tests verify edge cases and formula correctness beyond what visible tests check.

7. **Real-world data application:** Using the Boston and Weekly datasets provides practical context for the resampling techniques.

### Recommendations

**Top 3 Priority Fixes:**

1. **Remove numerical values from visible test assertions.** This is the most critical issue affecting academic integrity. Move all specific numerical checks to hidden tests and use structural/type checks in visible tests.

2. **Add data file documentation.** Clarify where the Boston and Weekly CSV files are located or how students should obtain them. Consider adding a setup cell that verifies data availability.

3. **Add context for the Boston dataset.** Explain what the variables represent and consider acknowledging the ethical issues with this dataset, or suggest an alternative dataset.
---
