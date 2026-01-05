---
## Critique: DATASCI 503, Homework 4: Classification

### Summary
- **Critical issues**: 2
- **Moderate issues**: 6
- **Minor issues**: 8

### Critical Issues

1. **Missing Section Header Before Problem 5**
   - **Location**: Between cell 11 (markdown about LDA Decision Boundary) and Problem 5 (cell 12)
   - **Description**: Cell 11 introduces a new section "LDA Decision Boundary" with setup information but is not formatted as a proper section header (should use `##` format). This breaks the structural flow.
   - **Why problematic**: Students may be confused about the relationship between this setup text and the following problems. The unmarked section transition is inconsistent with the rest of the document.
   - **Suggested fix**: Convert cell 11 to a proper section header with `##` formatting, e.g., `## LDA Decision Boundary` followed by the setup paragraph.

2. **Hidden Test References Undefined Variables in Problem 5**
   - **Location**: Cell 14 (test cell for Problem 5)
   - **Description**: The hidden test references `mu1` and `mu2` which are defined inside the `# BEGIN SOLUTION` block, not available in the student version.
   - **Why problematic**: When running the student version, this hidden test will fail with a `NameError` because `mu1` and `mu2` are not defined in the test cell's scope.
   - **Suggested fix**: Use hardcoded values in the hidden test: `assert boundary_c == (-1 + 3) / 2` or define the parameters outside the solution block.

### Moderate Issues

1. **Inconsistent Problem Numbering Flow**
   - **Location**: Problems 1-4 (theory/computation), then unnumbered section, then Problems 5-9 (LDA boundary), then section break, Problems 10-12 (Smarket), then section break, Problems 13-21 (Auto)
   - **Description**: The assignment has 21 problems across different sections but lacks clear section headers with `##` formatting for all topic transitions.
   - **Suggestion**: Add consistent `##` section headers: "## Theoretical Foundations" (Problems 1-4), "## LDA Decision Boundary" (Problems 5-9), "## Stock Market Prediction" (Problems 10-12), "## Auto MPG Classification" (Problems 13-21).

2. **Problem 14 Has Vague Requirements**
   - **Location**: Cell 41 (Problem 14)
   - **Description**: The problem asks students to identify "four quantitative features" but doesn't clarify whether origin should be considered quantitative. It also doesn't specify what constitutes a sufficient defense.
   - **Suggestion**: Clarify: "Choose four quantitative features from: cylinders, displacement, horsepower, weight, acceleration, and year. Justify each selection with a specific observation from your plots."

3. **Test Cell in Problem 14 Missing**
   - **Location**: After cell 42-43
   - **Description**: Problem 14 requires students to select features and create plots, but there is no test cell to verify the exploration was completed or validate the feature selection.
   - **Suggestion**: Add a basic test that checks the figure was created, or add structure asking students to store their selected features in a list that can be tested.

4. **Problem 10 Has No Test Cell**
   - **Location**: After cells 28-29
   - **Description**: Problem 10 asks for EDA but has no test assertions to verify completion.
   - **Suggestion**: Either add a test cell that validates a figure was created, or explicitly mark this as a free-response problem that doesn't require tests.

5. **Visible Test May Guide Solution in Problem 9**
   - **Location**: Cell 24
   - **Description**: The visible test reveals that there should be exactly 2 boundaries, the first negative and the second positive. This gives away structural information about the solution.
   - **Suggestion**: Make the assertion about the number of boundaries a hidden test, or rephrase the problem to explicitly state "find the two boundary points."

6. **Data File Paths Not Verified**
   - **Location**: Cells 26 and 37
   - **Description**: The assignment loads data from `./data/Smarket.csv` and `./data/auto_nonan.csv` but there's no verification or helpful error message if these files don't exist.
   - **Suggestion**: Add a markdown cell explaining where students can obtain these datasets, or add a try/except block with a helpful error message.

### Minor Issues

- **Problem 3**: The question uses "True or False" format in part (c) but other parts use open-ended format. Consider consistency.

- **Problem 4**: The hint mentions Bayes' theorem but the formula uses $P(D|X)$ notation without defining $D$ (dividend) explicitly in the setup.

- **Problem 5**: The instruction says "Make sure you label the axes" but doesn't specify whether a legend is required.

- **Problem 11**: The problem doesn't remind students which variables are available in the dataset or point them to look at the data frame structure.

- **Problem 13**: The threshold of 25 for mpg01 seems arbitrary. Consider adding context about why this threshold was chosen (e.g., median, historical significance).

- **Problem 15**: The problem specifies exact features to use ("the four selected features") but students haven't officially "selected" them yet - their selection in Problem 14 is qualitative. This could cause confusion if a student chose different features.

- **Problem 20**: The range 1-35 for K values seems arbitrary. Consider explaining why this range was chosen or asking students to explore and justify their own range.

- **Cell 1 (imports)**: The assignment suppresses all warnings with `warnings.filterwarnings("ignore")` which may hide useful information from students about deprecated functions or convergence issues.

### Strengths

1. **Well-Structured Progression**: The assignment builds logically from theoretical derivations (Problems 1-3) to computational applications (Problem 4) to practical implementations (Problems 5-21).

2. **Good Balance of Theory and Practice**: Combines mathematical derivations, conceptual questions, and hands-on coding tasks effectively.

3. **Comprehensive Coverage**: Covers LDA, QDA, logistic regression, and KNN, allowing meaningful comparisons between methods.

4. **Helpful Hints**: Most theoretical problems include hints that guide students toward the solution without giving it away (e.g., Problem 1's hint about taking the log).

5. **Clear Test Structure**: Most coding problems have well-formatted test cells with descriptive error messages and appropriate hidden tests.

6. **Real-World Datasets**: Uses practical datasets (S&P 500 returns, Auto MPG) that contextualize the methods being taught.

7. **Appropriate Solution Markers**: Consistently uses the correct `# BEGIN SOLUTION` / `# END SOLUTION` and `> BEGIN SOLUTION` / `> END SOLUTION` markers for code and markdown respectively.

### Recommendations

1. **Fix the undefined variable bug in Problem 5's hidden test** - This will cause autograding failures for correct student solutions. Replace `mu1` and `mu2` with their literal values (-1 and 3).

2. **Add section headers and test cells for exploratory problems** - Problems 10 and 14 should either have basic test cells or be explicitly marked as free-response problems. Add `##` section headers to clearly delineate the four main parts of the assignment.

3. **Clarify the feature selection flow in the Auto section** - Either make Problem 14 store the selected features in a variable that Problem 15 uses, or explicitly state the four features to use in Problem 15 so students with different EDA conclusions can still complete the assignment correctly.
---
