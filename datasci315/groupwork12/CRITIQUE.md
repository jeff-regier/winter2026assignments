---
## Critique: DATASCI 315, Group Work 12: Los Angeles Traffic Prediction with Graph Neural Networks

### Summary
- **Critical issues**: 3
- **Moderate issues**: 8
- **Minor issues**: 7

### Critical Issues

1. **Free-Response Problem Uses Incorrect Solution Markers**
   - **Location**: Cell 20 (Problem 1 markdown answer cell)
   - **Description**: The free-response solution uses `<!-- BEGIN SOLUTION -->` HTML comment syntax instead of the required blockquote-style markers (`> BEGIN SOLUTION` / `> END SOLUTION`).
   - **Why problematic**: The `make_student_version.py` validator will not recognize this as a solution block. The solution content will not be stripped when generating the student version, exposing answers to students.
   - **Suggested fix**: Replace `<!-- BEGIN SOLUTION -->` with `> BEGIN SOLUTION` and `<!-- END SOLUTION -->` with `> END SOLUTION`, ensuring two newlines after the opening marker.

2. **Missing Documentation Links for Key External Repository**
   - **Location**: Cell 6 (cloning stgat_traffic_prediction repo)
   - **Description**: The assignment clones an external repository without any verification that the repository still exists or that its structure matches what the assignment expects. No link to the repository is provided for students to inspect.
   - **Why problematic**: If the repository is deleted, moved, or modified, the entire assignment will break. Students have no way to troubleshoot or understand the repository structure. This is a significant dependency risk.
   - **Suggested fix**: Add a visible link to `https://github.com/jswang/stgat_traffic_prediction`, include a note about what commit/version is expected, and consider adding error handling or instructions for if the clone fails.

3. **`os.chdir()` Changes Working Directory Without Restoration**
   - **Location**: Cell 6
   - **Description**: The code changes the current working directory with `os.chdir(repo_path)` but never restores it. This can cause issues with relative paths in subsequent cells and breaks notebook reproducibility if cells are run out of order.
   - **Why problematic**: If a student re-runs earlier cells after this point, paths may not resolve correctly. This is a fragile pattern that can cause confusing errors.
   - **Suggested fix**: Use absolute paths throughout instead of `os.chdir()`, or document clearly that the working directory changes and provide a way to reset it.

### Moderate Issues

1. **Problem 1 Test Cell Is Too Weak**
   - **Location**: Cell 22
   - **Description**: The test only checks that `problem_1_completed = True` is set. There's no validation that students actually wrote meaningful answers about TensorBoard metrics.
   - **Suggestion**: Add a comment in the hidden tests explaining that manual grading is required, or add checks for markdown cell content length to ensure students wrote substantive answers.

2. **Missing GPU Fallback Guidance**
   - **Location**: Cells 3-4 and throughout
   - **Description**: The assignment says "it would be helpful to select GPU as the runtime" but training 60 epochs on CPU would take prohibitively long. There's no guidance for students without GPU access.
   - **Suggestion**: Either provide estimated training times for CPU vs GPU, reduce epochs for CPU fallback, or explicitly state that GPU is required (not just helpful).

3. **Hidden Tests Give Away Solution Pattern in Problem 2**
   - **Location**: Cell 27 (Problem 2a hidden tests)
   - **Description**: The visible test reveals that there should be "6 directed edges" for the linear graph, which tells students the exact edge count to target.
   - **Suggestion**: Make the visible test more general (e.g., "check graph is connected") and move the specific edge count to hidden tests.

4. **Problem 3 Uses Undefined Device Handling**
   - **Location**: Cell 41
   - **Description**: The solution uses `.cpu().numpy()` but this pattern isn't demonstrated elsewhere in the assignment and may confuse students about when device transfers are needed.
   - **Suggestion**: Add a brief comment explaining why `.cpu()` is needed before `.numpy()` or provide this as starter code.

5. **Problem 4 Parts Are Not Clearly Scaffolded**
   - **Location**: Cells 45-67
   - **Description**: Problem 4 has six parts (a-f) but jumps quickly from simple concepts (randperm, argsort) to complex graph permutation. Part (f) is significantly harder than earlier parts with minimal scaffolding.
   - **Suggestion**: Add more intermediate hints in Part (f), provide pseudocode, or break down the steps more explicitly.

6. **Deprecated API: `resize_()` Method**
   - **Location**: Cell 8 (TrafficDataset.process method)
   - **Description**: The code uses `tensor.resize_()` which is deprecated and may be removed in future PyTorch versions. Modern PyTorch uses `tensor = tensor[:, :num_edges]` or similar slicing.
   - **Suggestion**: Update to use slicing or `narrow()` instead of `resize_()`.

7. **Missing Error Messages in Some Visible Assertions**
   - **Location**: Cells 42, 47, 53
   - **Description**: Some assertions have descriptive error messages, but others don't. For example, Cell 47 has `assert idx_perm.shape == torch.Size([4]), "..."` but the second assertion lacks context.
   - **Suggestion**: Ensure all visible assertions have descriptive error messages to help students debug.

8. **Empty Markdown Cell**
   - **Location**: Cell 43
   - **Description**: There's an empty markdown cell between Problem 3 and the Equivariance section.
   - **Suggestion**: Either remove this cell or add appropriate content/spacing.

### Minor Issues

- **Cell 37**: Empty code cell with no purpose.
- **Problem header inconsistency**: Some problems use `### Problem N:` while sub-parts use `#### Part (a):` - this is fine but the pattern should be documented if intentional.
- **Cell 12**: The `eval_model` function has redundant `torch.no_grad()` decorator and a `with torch.no_grad():` context manager inside.
- **Cell 16**: Missing docstring for the `writer = SummaryWriter()` explaining what runs directory is used.
- **Cell 24**: The `config` dictionary could benefit from a brief comment explaining each hyperparameter's purpose for educational value.
- **Inconsistent import organization**: Some cells re-import modules already imported earlier (e.g., `torch` is imported multiple times).
- **Cell 10**: The `StGat` class initializes `self.lstm1` parameters twice in a row (lines with `for name, param in self.lstm1.named_parameters()` appear twice, likely a copy-paste error where the second should be `self.lstm2`).

### Strengths

1. **Excellent introductory context**: The assignment provides clear, well-written background on the traffic prediction problem, the dataset, and the ST-GAT method with appropriate academic citation.

2. **Strong pedagogical structure**: The assignment follows a logical flow from data loading through model training to testing, with clear section headers.

3. **Good use of visualization**: TensorBoard integration and matplotlib plots help students understand model behavior and results.

4. **Progressive complexity**: Problems build from simple graph construction (Problem 2) to understanding model properties (Problem 4).

5. **Real-world relevance**: Using actual LA traffic data makes the assignment engaging and demonstrates practical applications of GNNs.

6. **Comprehensive documentation links**: References to PyTorch Geometric documentation help students learn to use official resources.

7. **Well-structured test cells**: Most test cells follow the expected format with visible assertions and hidden tests.

### Recommendations

**Top 3 Priority Fixes:**

1. **Fix the free-response solution markers in Problem 1** - This is a structural conformance issue that will cause the student version generator to fail. Change from HTML comments to blockquote-style markers immediately.

2. **Fix the LSTM initialization bug** - In Cell 10, the second initialization loop incorrectly references `self.lstm1` instead of `self.lstm2`. This could affect model training behavior.

3. **Add GPU requirement clarity and error handling for external repository** - Students need clear guidance on runtime requirements, and the assignment should handle the case where the external repository fails to clone gracefully.

---
