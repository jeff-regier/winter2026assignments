---
## Critique: DATASCI 315, Group Work 11: LLM Few-Shot Learning and Fine-Tuning

### Summary
- **Critical issues**: 3
- **Moderate issues**: 6
- **Minor issues**: 5

### Critical Issues

1. **Bug in compute_metrics function - torch.mean on list**
   - **Location**: Cell 41
   - **Description**: The code uses `torch.mean(exact_matches)` where `exact_matches` is a Python list of integers, not a tensor. This will raise a TypeError.
   - **Why problematic**: The compute_metrics function will crash if students try to use it for evaluation during training. This is provided code that students are expected to rely on.
   - **Suggested fix**: Replace `exact_match_score = torch.mean(exact_matches)` with `exact_match_score = sum(exact_matches) / len(exact_matches)` or convert to tensor first with `torch.tensor(exact_matches).float().mean()`.

2. **Bug in sample code - torch.randint missing syntax**
   - **Location**: Cell 72
   - **Description**: The code `torch.randint(0, len(predicted_dataset), 5, replace=False).astype(int)` is incorrect. `torch.randint` takes a size tuple as the third argument and doesn't have a `replace` parameter. The `.astype(int)` method is NumPy syntax, not PyTorch.
   - **Why problematic**: This cell will crash when students run it, preventing them from examining their predictions.
   - **Suggested fix**: Replace with `torch.randperm(len(predicted_dataset))[:5].tolist()` or use `random.sample(range(len(predicted_dataset)), 5)`.

3. **Problem 3 has no solution markers or test cell**
   - **Location**: Cell 75
   - **Description**: Problem 3 only has a comment `# Your fine-tuning task implementation here` with no `# BEGIN SOLUTION` / `# END SOLUTION` markers and no test cell following it.
   - **Why problematic**: Violates the assignment conventions. The `make_student_version.py` validator will fail, and there's no autograding structure for this problem.
   - **Suggested fix**: Add proper solution markers and a test cell that verifies basic elements (dataset creation, training, and metric comparison).

### Moderate Issues

1. **Missing `strict=True` parameter handling may cause issues**
   - **Location**: Cell 41
   - **Description**: The `strict=True` in `zip(decoded_preds, decoded_labels, strict=True)` requires Python 3.10+. While likely fine for most setups, this could cause compatibility issues.
   - **Suggestion**: Either document Python version requirement or remove `strict=True`.

2. **Data file paths are hardcoded without existence check**
   - **Location**: Cells 31, 35
   - **Description**: The code assumes files exist at `./data/grammar_train.json`, etc. If students haven't downloaded files or placed them in the wrong location, they'll get confusing errors.
   - **Suggestion**: Add a check for file existence with a helpful error message, or provide code to download the files programmatically.

3. **Problem 1 test cell is too weak**
   - **Location**: Cell 26
   - **Description**: The test only checks that `few_shot_prompt` exists and has >50 characters. It doesn't verify the prompt has examples, a task structure, or that the model was actually run.
   - **Suggestion**: Add tests for: (1) multiple examples in prompt, (2) generation was performed, (3) output was produced.

4. **Problem 2 test cell doesn't verify BLEU threshold**
   - **Location**: Cell 57
   - **Description**: The test only checks that `training_args` exists and epochs >= 1. The actual requirement (BLEU >= 0.9) is not verified programmatically.
   - **Suggestion**: Add a test cell after cell 70 that asserts `bleu_result['bleu'] >= 0.9` with a descriptive error message.

5. **No documentation links for key concepts**
   - **Location**: Throughout
   - **Description**: The assignment introduces several complex concepts (T5, BLEU, few-shot learning, fine-tuning) but doesn't link to documentation or further reading.
   - **Suggestion**: Add links to Hugging Face T5 documentation, the original T5 paper, and BLEU metric explanation.

6. **Deprecated/changing API warning**
   - **Location**: Cell 41
   - **Description**: Using `labels != -100` with tensor comparison may produce warnings in newer versions. Also, `T5Tokenizer` may show deprecation warnings suggesting `T5TokenizerFast`.
   - **Suggestion**: Consider using `T5TokenizerFast` or add a note about expected warnings.

### Minor Issues

- **Cell 41**: `labels` is reassigned from tuple element to tensor, which is confusing variable shadowing.
- **Cell 56**: The solution provides complete hyperparameters, making it easy to just use these values. Consider providing partial solution or ranges.
- **Cell 13**: The semicolon in `model.eval();` is unusual Python style (used to suppress output in notebooks but looks like JavaScript).
- **Cell 72**: Uses `torch.randint` but earlier cells show similar patterns - consider using consistent random sampling approach.
- **Inconsistent model naming**: Uses `flan-t5-base` for Part 1 and `t5-small` for Part 2 without explaining the difference or trade-offs.

### Strengths

1. **Clear structure**: The assignment is well-organized with distinct parts for few-shot learning and fine-tuning, building complexity progressively.

2. **Good conceptual explanations**: Each section has clear explanations of what few-shot learning and fine-tuning are and how they differ.

3. **Creative open-ended problems**: Problems 1 and 3 encourage creativity while Problem 2 provides a concrete, achievable goal.

4. **Complete working example**: Part 1 provides a fully functional example of few-shot translation that students can learn from.

5. **Practical real-world task**: Grammar correction is a relatable and useful NLP task that students can understand and experiment with.

6. **Good scaffolding**: The assignment provides most of the infrastructure code, letting students focus on understanding the concepts and tuning parameters.

### Recommendations

1. **Fix the critical bugs immediately**: The `torch.mean` on list (cell 41) and `torch.randint` syntax error (cell 72) will cause runtime crashes. These must be fixed before students attempt the assignment.

2. **Add proper structure for Problem 3**: Add `# BEGIN SOLUTION` / `# END SOLUTION` markers and a test cell. Even for open-ended problems, having structure ensures the validator works and provides some autograding capability.

3. **Add a test for the BLEU >= 0.9 requirement**: After cell 70, add an assertion that programmatically verifies the goal was achieved, with a helpful error message if not.
---
