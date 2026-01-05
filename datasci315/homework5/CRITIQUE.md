---
## Critique: Homework 5 - Shallow Networks, Loss Functions, and Fitting (Concepts and Theory)

### Summary
- **Critical issues**: 3
- **Moderate issues**: 3
- **Minor issues**: 2

### Critical Issues

1. **Problem Statements Are Missing**
   - **Location**: All problem cells (Problems 1-8)
   - **Description**: Every problem simply references a UDL exercise number (e.g., "UDL 3.4") without including the actual problem statement. Students must have the textbook open to understand what they are being asked to do.
   - **Why problematic**: This creates a poor user experience and makes the assignment inaccessible to anyone without the textbook. It also makes the notebook non-self-contained, which is poor pedagogical practice. If the textbook version changes or becomes unavailable, the assignment becomes unusable.
   - **Suggested fix**: Include the full problem statement (or a paraphrased version if copyright is a concern) directly in the notebook for each problem. At minimum, provide a brief summary of what each problem asks.

2. **No Pedagogical Scaffolding or Hints**
   - **Location**: All problems
   - **Description**: There are no hints, worked examples, or guidance provided for any of the 8 problems. The assignment simply lists exercise numbers.
   - **Why problematic**: Students working on theory problems often benefit from hints about approaches, relevant formulas, or pointers to specific sections of the textbook. Without any scaffolding, struggling students have no starting point.
   - **Suggested fix**: Add hints for each problem (e.g., "Hint: Consider the number of linear regions a ReLU network can create" or "Hint: Review the derivation of cross-entropy loss in Section 5.2"). Include at least one worked example in the introduction showing how to approach a similar theory problem.

3. **PDF Submission Instructions May Cause Confusion**
   - **Location**: Cell 2 (introduction)
   - **Description**: The assignment says to "upload a PDF file containing them to Canvas" but the assignment is delivered as a Jupyter notebook with solution markers. It's unclear whether students should write solutions in the notebook and then export to PDF, or write solutions separately.
   - **Why problematic**: This creates ambiguity about the submission format and workflow. The solution markers (`> BEGIN SOLUTION` / `> END SOLUTION`) suggest in-notebook solutions, but the instructions suggest a separate PDF.
   - **Suggested fix**: Clarify the workflow explicitly. Either: (a) tell students to write solutions in the notebook markdown cells and export to PDF, or (b) remove the solution markers and provide a separate template, or (c) provide both options with clear instructions for each.

### Moderate Issues

1. **No Link to the Textbook**
   - **Location**: Cells 1-2 (introduction)
   - **Description**: The textbook "Understanding Deep Learning" is mentioned but no link is provided.
   - **Suggestion**: Add a direct link to the textbook (https://udlbook.github.io/udlbook/) so students can easily access the relevant chapters and problems.

2. **No Learning Objectives or Expected Outcomes**
   - **Location**: Introduction section
   - **Description**: While the topics are mentioned (shallow networks, loss functions, fitting), there are no specific learning objectives stating what students should be able to do after completing the assignment.
   - **Suggestion**: Add 3-5 learning objectives such as: "After completing this assignment, you should be able to: (1) Calculate the number of parameters in a shallow network, (2) Derive the gradient of common loss functions, (3) Explain why gradient descent converges to local minima."

3. **No Estimated Time or Difficulty Indication**
   - **Location**: Introduction
   - **Description**: Students have no indication of how long this assignment should take or the relative difficulty of problems.
   - **Suggestion**: Add an estimated completion time and/or indicate which problems are more challenging so students can plan accordingly.

### Minor Issues

- **Solution placeholder formatting**: The solution placeholders use "*Write your solution here.*" in italics, but for free-response markdown cells, plain text might be clearer.
- **Section headers could include page numbers**: Since students need to look up problems in the textbook, including page numbers or section references (e.g., "UDL 3.4 (page 45)") would save time.

### Strengths

1. **Clear structural organization**: The assignment is well-organized by textbook chapter (Chapter 3, 5, 6), making it easy to understand the topic progression.
2. **Good topic coverage**: The selected chapters provide a logical progression from network architecture to loss functions to optimization.
3. **Correct solution marker format**: The free-response solution markers (`> BEGIN SOLUTION` / `> END SOLUTION`) follow the correct blockquote format specified in CLAUDE.md.
4. **Appropriate scope**: 8 theory problems is a reasonable amount for a homework assignment.
5. **Good contextual introduction**: The first cell provides helpful context about why these topics matter for later practical work.

### Recommendations

**Top 3 Priority Fixes:**

1. **Include full problem statements**: This is essential for the assignment to be usable. Either copy the problem text directly or write equivalent problems that cover the same concepts.

2. **Add hints and scaffolding**: For each problem, add at least one hint pointing to relevant concepts, formulas, or textbook sections. Consider adding a worked example in the introduction.

3. **Clarify submission workflow**: Explicitly state whether students should write in the notebook and export to PDF, or create a separate document. Remove ambiguity between the notebook solution markers and PDF submission instructions.

---
