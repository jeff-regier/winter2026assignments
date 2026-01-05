# Critique Assignment

You are reviewing a course assignment to provide a thorough critique. Your goal is to identify issues, assess quality, and provide actionable feedback. **Do NOT modify any files.**

## Required Argument

The user must provide a file path: `/critique-assignment <filepath>`

## Review Process

### 1. Read the Assignment
Read the entire assignment file to understand its structure and content.

### 2. Analyze Each Dimension

Check each dimension below and note any issues found:

#### A. Clarity & Ambiguity
- **Unclear requirements**: Are expected inputs/outputs well-defined?
- **Ambiguous phrasing**: Could students reasonably interpret this multiple ways?
- **Missing edge cases**: Are boundary conditions specified when relevant?
- **Indexing ambiguity**: Is it clear whether indices are 0-based or 1-based?
- **Unclear data types**: Are expected types specified?

#### B. Pedagogical Quality
- **Missing hints**: Do complex problems have helpful hints?
- **Missing worked examples**: Do algorithmic problems show step-by-step reasoning?
- **Difficulty progression**: Are there steep jumps between problems?
- **Lack of scaffolding**: Are complex tasks broken into manageable steps?
- **Missing prerequisites**: Are assumed skills stated?
- **Missing documentation links**: Are relevant resources linked?
- **Syntax over understanding**: Do problems test rote syntax rather than concepts?

#### C. Test Quality
- **Missing error messages**: Do assertions have descriptive failure messages?
- **Missing edge cases**: Do tests cover boundary conditions?
- **Weak tests**: Could tests pass with incorrect implementations?
- **Solution giveaway**: Do visible tests reveal the solution approach? (Note: Hidden tests CANNOT give away solutions since students never see them - only flag this for visible tests)
- **Insufficient coverage**: Does each problem have at least 2 visible tests?
- **Identical hidden tests**: Hidden tests can check similar things as visible tests, but should not be exactly identical (to prevent students from hardcoding answers). Hidden tests CAN check specific expected values or outcomes without concern about "revealing" solutions.

Note: Free-response problems (using blockquote solution markers in markdown cells) are manually graded and do not require test cells. This is expected behavior.

#### D. Code Quality (in provided examples/starter code)
- **Poor variable names**: Single-letter names (except i, j, k for loops)?
- **Anti-patterns**: Is bad practice being taught?
- **Non-idiomatic code**: Are library idioms ignored (e.g., loops instead of vectorized ops)?

Note: Do NOT critique solution code, as students won't necessarily see it. Only critique code that students will see (examples, starter code, hints).

#### E. Writing Quality
- **Grammar/spelling**: Any errors?
- **Inconsistent terminology**: Are different terms used for the same concept?
- **Verbose explanations**: Could text be more concise?
- **Poor formatting**: Are headers, code blocks, math notation correct?

#### F. Structural Conformance
- **Missing solution markers**: Are `# BEGIN SOLUTION` / `# END SOLUTION` present?
- **Test cell format**: Do test cells start with `# Test assertions`?
- **Problem header format**: Are headers `### Problem N: Title`?
- **Mixed cells**: Are solution code and tests in the same cell?
- **Execution dependencies**: Do cells depend on non-obvious execution order?

#### G. Content Accuracy
- **Incorrect outputs**: Are expected values in tests correct?
- **Deprecated APIs**: Are outdated functions used?
- **Dead links**: Do documentation links work?
- **Math errors**: Are formulas and calculations correct?

#### H. Assignment-Level Issues
- **Excessive length**: Is the assignment too long for the allotted time?
- **Topic drift**: Does the assignment lose focus?
- **Redundant problems**: Do multiple problems test the same concept?
- **Imbalanced types**: Is there a good mix of code and free-response?
- **Poor flow**: Do problems integrate naturally with lessons? Ideally, assignments should flow well with problems interspersed among teaching content, making clear how lessons and topics relate to each other. Problems should feel like natural extensions of the material just covered, not disconnected exercises.

#### I. Tone & Professionalism
- **Threatening language**: Does the assignment use warnings or threats toward students (e.g., "DO NOT COPY" warnings, threats of zeros)? Assignments should treat students with respect and assume good faith.
- **Unprofessional tone**: While assignments don't need to be overly formal, they should maintain a professional and collegial tone appropriate for higher education.
- **Condescending language**: Does the text talk down to students or assume incompetence?
- **Inconsistent register**: Does the tone shift awkwardly between formal and informal?

### 3. Classify Issues by Severity

**Critical**: Would cause student confusion, grading failures, or incorrect learning
- Ambiguous requirements with no clear interpretation
- Tests that pass with wrong implementations
- Incorrect expected outputs
- Missing solution markers (breaks autograding)

**Moderate**: Reduces quality but doesn't block completion
- Missing hints or worked examples
- Poor variable naming
- Verbose or unclear explanations
- Missing edge case tests
- Threatening or unprofessional language
- Poor assignment flow (problems disconnected from lessons)

**Minor**: Polish items and suggestions
- Typos and grammar
- Formatting inconsistencies
- Could-be-better phrasing

## Output Format

Print your critique in this format:

---

## Critique: [Assignment Name]

### Summary
- **Critical issues**: X
- **Moderate issues**: Y
- **Minor issues**: Z

### Critical Issues

**[Issue Title]** (Problem N / Section)
- Description of the issue
- Why it's problematic
- Suggested fix

[Repeat for each critical issue]

### Moderate Issues

**[Issue Title]** (Location)
- Description and suggestion

[Repeat for each moderate issue]

### Minor Issues

- [Brief description] (Location)
- [Brief description] (Location)

### Strengths

- [What the assignment does well]
- [Good pedagogical choices]

### Recommendations

1. [Highest priority fix]
2. [Second priority]
3. [Third priority]

---

## Important Guidelines

- **Do NOT modify any files** - this is a read-only review
- **Be specific** - cite problem numbers and quote problematic text
- **Be constructive** - focus on actionable improvements
- **Be thorough** - check every dimension systematically
- **Be fair** - acknowledge what works well
