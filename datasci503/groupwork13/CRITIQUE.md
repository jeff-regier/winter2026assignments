---
## Critique: DATASCI 503, Group Work 13: Autoencoders with MNIST

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

#### 1. Missing Required Test Assertions Format
**Location:** Problem 4 (cells 15-17), Problem 7 (cell 29), Problem 10 answer (cell 42), Problem 11 answer (cell 46)

**Description:** Free-response problems lack test cells entirely. While the CLAUDE.md guidelines indicate that free-response problems using blockquote-style markers don't require test cells, the current formatting is inconsistent. Some free-response answers have `> BEGIN SOLUTION` on the same line as text rather than on its own line.

**Why problematic:** The validator may not properly recognize these as free-response problems, and the inconsistent formatting could cause issues with student version generation.

**Suggested fix:** Ensure all free-response solutions have `> BEGIN SOLUTION` followed by two newlines before the answer text, as specified in CLAUDE.md:
```markdown
> BEGIN SOLUTION

Your answer text here.

> END SOLUTION
```

#### 2. Problem 5 Test Cell References Undefined Variables in Student Version
**Location:** Cell 20 (test assertions for Problem 5)

**Description:** The test cell references `latent_x` and `latent_y` which are defined in the solution block. When the student version is generated, these variables will be undefined, causing the tests to fail immediately.

**Why problematic:** Students cannot run the test cell to check their work because the tests reference solution-specific variable names that may not exist in student code.

**Suggested fix:** Either:
1. Move the variable definitions outside the solution block as starter code
2. Modify tests to check for the existence of a meshgrid or plot without relying on specific variable names
3. Use try/except to provide better error messages if variables are missing

---

### Moderate Issues

#### 1. Problem 3 Function Name Inconsistency
**Location:** Cell 10 (problem description) vs Cell 11 (implementation)

**Description:** The problem description mentions `train_AE` but the actual function is named `train_autoencoder`. This inconsistency could confuse students.

**Suggestion:** Update the problem description to reference `train_autoencoder` consistently.

#### 2. Problem 6 Missing Test Coverage for Function Behavior
**Location:** Cell 24

**Description:** The test cell only checks function signature parameters, not that the function actually produces the expected interpolation behavior. Students could pass tests with a non-functional implementation.

**Suggestion:** Add hidden tests that verify the function produces outputs (e.g., check that matplotlib figures are created or that the function runs without error with valid inputs).

#### 3. Problem 9 Training with Only 5 Epochs
**Location:** Cell 37

**Description:** The VAE is trained for only 5 epochs (`num_epochs=5`), which is likely insufficient for meaningful learning. This contrasts with the autoencoder training in Problem 3 which uses 100 epochs.

**Suggestion:** Either increase the epochs or add a note explaining why fewer epochs are used (e.g., time constraints during lab). Consider using `num_epochs=50` or explaining that students can increase this value for better results.

#### 4. Problem 11 Test Cell References Solution Variable
**Location:** Cell 45

**Description:** The test cell references `approx_posterior` which is defined in the solution. In the student version, if a student names this variable differently, the tests will fail with a confusing error.

**Suggestion:** Add clearer variable naming requirements in the problem description, or restructure tests to be more flexible.

#### 5. Missing Shuffling Specification in Problem 1
**Location:** Cell 4

**Description:** The problem doesn't specify whether DataLoaders should shuffle data. The solution shuffles train_loader but not val_loader and test_loader, but this isn't mentioned in requirements.

**Suggestion:** Add explicit instruction: "The train_loader should shuffle data, while val_loader and test_loader should not."

#### 6. Problem 8 Missing Architecture Guidance
**Location:** Cell 31

**Description:** The problem asks students to implement a VAE but doesn't specify the network architecture dimensions, unlike Problem 2 which gives clear guidance on layer structure.

**Suggestion:** Either provide expected architecture (e.g., "Use 512 -> 256 for encoder, output mu and logvar") or explicitly state that students can choose their own architecture.

---

### Minor Issues

- **Cell 3:** The phrase "raw direction of the data" is unclear. Consider rephrasing to "original feature dimensions."

- **Cell 3:** The autoencoder link to GeeksforGeeks could be supplemented with more authoritative sources (e.g., PyTorch tutorials, academic references).

- **Cell 10:** Typo: "that states what the current epoch" should be "that shows the current epoch" for better grammar.

- **Cell 21:** The function name in the hint says "extrapolate_digits" but the operation being performed is interpolation, not extrapolation. This is conceptually misleading.

- **Cell 30:** The KL divergence formula uses $\sigma^2$ in some places and $\sigma$ in others without clear distinction. The implementation uses `logvar` which should be explicitly connected to these formulas.

- **Cell 30:** The ELBO formula has a sign error - it should be minus KL divergence (maximizing ELBO), or the explanation should clarify this is the loss (negative ELBO).

- **Cell 34:** Same typo as Cell 10: "that states what the current epoch" should be "that shows the current epoch."

- **Problem 5:** The variable `NUM_IMAGES` is provided but never used in a meaningful way in the tests.

---

### Strengths

1. **Well-structured progression:** The assignment builds logically from basic autoencoders to VAEs, with each problem building on previous concepts.

2. **Strong theoretical exposition:** The explanation of VAEs in Cell 30 provides excellent mathematical background with derivations and external references.

3. **Good test coverage:** Most problems have both visible and hidden tests with descriptive error messages.

4. **Practical applications:** Problems 5, 6, 10, and 11 provide excellent visualization exercises that help students understand latent spaces intuitively.

5. **Appropriate scaffolding:** Helper functions like `get_test_digit` reduce cognitive load and let students focus on core concepts.

6. **Consistent formatting:** Problems follow the required header format (`### Problem N: Title`) throughout.

7. **Good free-response questions:** The conceptual questions in Problems 4, 7, 10, and 11 reinforce understanding of why these techniques matter.

---

### Recommendations

**Top 3 Priority Fixes:**

1. **Fix Problem 5 test cell:** Restructure tests so they don't depend on solution-specific variable names, or provide the variable names as starter code outside the solution block.

2. **Standardize free-response formatting:** Ensure all blockquote solution markers have proper newlines so the validator correctly identifies them as free-response problems.

3. **Fix function name inconsistency:** Update Problem 3 description to reference `train_autoencoder` instead of `train_AE` to avoid student confusion.

---
