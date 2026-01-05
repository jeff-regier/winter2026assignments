---
## Critique: Homework 10 - CNN Concepts and Theory

### Summary
- **Critical issues**: 3
- **Moderate issues**: 3
- **Minor issues**: 2

### Critical Issues

1. **Problems lack self-contained descriptions**
   - **Location**: All problems (1-8)
   - **Description**: Every problem simply states "Refer to Problem X.X in *Understanding Deep Learning*, Chapter 10" without including the actual problem text. Students must have the textbook open to complete this assignment.
   - **Why problematic**: This creates accessibility issues for students who may not have immediate access to the textbook. It also makes the assignment impossible to complete without external resources, and prevents the assignment from being a standalone document. Additionally, this makes grading more difficult as TAs/graders also need the textbook.
   - **Suggested fix**: Include the full problem statement (or a summary) for each problem within the notebook. If copyright is a concern, paraphrase the problems or write original problems inspired by the textbook concepts.

2. **No scaffolding or hints provided**
   - **Location**: All problems (1-8)
   - **Description**: The assignment provides no hints, worked examples, or guidance for any of the eight problems. Students are simply given empty solution blocks.
   - **Why problematic**: Theoretical problems on CNN concepts (convolution operations, pooling, translation equivariance) can be challenging. Without any scaffolding, students may struggle to know where to start or what level of detail is expected. This is especially problematic for a homework assignment that students complete independently.
   - **Suggested fix**: Add hints for each problem (e.g., "Hint: Consider what happens to the receptive field as you add more convolutional layers"). Include at least one worked example in the introduction showing the expected format and depth of a solution.

3. **No indication of problem difficulty or expected response length**
   - **Location**: All problems (1-8)
   - **Description**: Students have no way to gauge how much time each problem should take or how detailed their responses should be.
   - **Why problematic**: Without guidance, some students may write excessively long responses while others may provide insufficient detail. This leads to inconsistent submissions and unfair grading.
   - **Suggested fix**: Add point values to each problem, and/or include guidance like "Write 2-3 paragraphs" or "Derive the equation and explain your reasoning in 1-2 sentences."

### Moderate Issues

1. **Free-response solution marker formatting issue**
   - **Location**: All solution blocks (cells 3, 5, 7, 9, 11, 13, 15, 17)
   - **Description**: The solution markers have only one newline after `> BEGIN SOLUTION` instead of two. The current format is:
     ```markdown
     > BEGIN SOLUTION

     *Your answer here.*
     > END SOLUTION
     ```
   - **Suggested fix**: Per CLAUDE.md conventions, there should be two newlines after `> BEGIN SOLUTION` so it renders on its own line. Update to:
     ```markdown
     > BEGIN SOLUTION


     *Your answer here.*

     > END SOLUTION
     ```

2. **No link to textbook or chapter resources**
   - **Location**: Introduction (cells 0-1)
   - **Description**: While the textbook is mentioned, no link is provided to access it online (if available) or to supplementary resources.
   - **Suggested fix**: Add a link to the textbook's official website or PDF if openly available. Include links to relevant lecture slides or supplementary materials that cover the same concepts.

3. **Missing submission instructions**
   - **Location**: End of notebook
   - **Description**: There are no instructions for how to submit the completed assignment.
   - **Suggested fix**: Add a final cell with submission instructions (e.g., "Save your notebook and submit to Canvas" or similar).

### Minor Issues

- **Title format**: The title "Homework 10" does not specify what topics the problems cover beyond "CNN Concepts and Theory." Consider making the title more specific (e.g., "Convolution, Pooling, and Translation Equivariance").
- **Introduction mentions "practical CNN implementations from earlier assignments"**: This assumes students have completed specific prior assignments. Consider adding a reference to which specific assignment(s) this builds upon.

### Strengths

1. **Consistent problem structure**: All problems follow the same format, making the assignment easy to navigate.
2. **Clear solution markers**: The free-response solution markers are correctly used (blockquote style), which will work with the student version generator.
3. **Good topic selection**: Chapter 10 of UDL covers fundamental CNN theory, and the selected problems (10.3, 10.4, 10.5, 10.8, 10.9, 10.10, 10.11, 10.14) appear to provide good coverage of key concepts.
4. **Appropriate use of theory-only format**: For a homework focused on mathematical understanding rather than coding, the free-response format is appropriate.

### Recommendations

**Top 3 priority fixes:**

1. **Include full problem statements**: Either reproduce the textbook problems (with attribution) or write equivalent original problems. The assignment must be self-contained.

2. **Add scaffolding and hints**: For each problem, provide at least one hint and indicate what concepts the problem is testing. Consider adding a worked example at the beginning to demonstrate the expected solution format.

3. **Add point values and expected response length**: Help students understand the relative importance and expected depth of each problem by adding point values (e.g., "[5 points]") and/or response length guidance.
---
