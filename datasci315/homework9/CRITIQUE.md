---
## Critique: DATASCI 315, Homework 9: Convolutional Neural Networks

### Summary
- **Critical issues**: 3
- **Moderate issues**: 7
- **Minor issues**: 5

### Critical Issues

#### 1. Missing import statement for `requests`
- **Location**: Cell 3 (Getting started section)
- **Description**: The code uses `requests.get(url, timeout=30)` but `requests` is never imported in the notebook.
- **Why problematic**: The notebook will fail immediately when students try to run it, creating a frustrating first experience.
- **Suggested fix**: Add `import requests` to the imports cell (cell 2).

#### 2. Flowchart images hosted on Google Drive may be inaccessible
- **Location**: Cells 14, 17, 20, 31 (Problems 3, 4, 6)
- **Description**: The flowchart images use Google Drive URLs (`https://drive.google.com/uc?id=...`). These may require authentication or may become unavailable if sharing settings change.
- **Why problematic**: Students cannot complete Problems 3, 4, and 6 without seeing the architecture diagrams. These are essential to understanding what they need to implement.
- **Suggested fix**: Host images in the repository or use a more reliable hosting solution. At minimum, provide detailed text descriptions of the architectures as fallbacks.

#### 3. MysteryBlock solution appears incorrect
- **Location**: Cell 18 (Problem 3)
- **Description**: The solution uses `self.pool1` twice with a MaxPool2d of kernel_size=3, but without seeing the flowchart, it's unclear if this matches the intended architecture. The pooling calculations `pool_out = ((height - 1) // 3 + 1, (width - 1) // 3 + 1)` assume stride=3, but MaxPool2d defaults to kernel_size as stride when not specified. Additionally, the solution creates `dense1` and `dense2` with different input sizes based on different pooling stages, which seems overly complex.
- **Why problematic**: The solution may not match the flowchart, and the visible test only checks one specific output value which could pass even with incorrect implementations.
- **Suggested fix**: Verify the solution matches the flowchart. Add more comprehensive tests that check intermediate layer behavior.

### Moderate Issues

#### 1. Problem 3 lacks architectural description
- **Location**: Cell 17 (Problem 3)
- **Description**: The problem only shows an image and says "fill in using the following flowchart." There is no text description of what layers are expected (number of conv layers, pooling type, filter sizes, etc.).
- **Suggestion**: Add a bulleted list describing the architecture in text form (e.g., "Two conv layers with 64 filters each, one max pooling layer, two dense layers...").

#### 2. Problem 4 has incomplete specification
- **Location**: Cell 20 (Problem 4)
- **Description**: The problem mentions `filters` is a "List of filter counts" but doesn't explain what happens when `self_conv=False` (2 filters) vs `self_conv=True` (3 filters). The relationship between filter list length and `self_conv` is implicit.
- **Suggestion**: Explicitly state: "When `self_conv=False`, `filters` should have 2 elements [f1, f2]. When `self_conv=True`, `filters` should have 3 elements [f1, f2, f3] where f3 is for the skip connection conv layer."

#### 3. No documentation links provided
- **Location**: Throughout the assignment
- **Description**: The assignment introduces several PyTorch concepts (nn.Module, Conv2d, BatchNorm2d, MaxPool2d, etc.) but provides no links to official PyTorch documentation.
- **Suggestion**: Add links to relevant PyTorch documentation, especially for nn.Conv2d, nn.BatchNorm2d, and the transforms module.

#### 4. Problem 6 training requires CUDA but no fallback provided
- **Location**: Cells 27, 34-37
- **Description**: The `train()` function hardcodes `.cuda()` calls, and the assignment mentions checking CUDA availability but provides no fallback for students without GPU access.
- **Suggestion**: Modify the train function to use device-agnostic code (`device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`) or provide instructions for Google Colab GPU setup earlier.

#### 5. Hidden tests in Problem 3 are weak
- **Location**: Cell 19 (Problem 3 test cell)
- **Description**: The hidden test only checks output shape for a different input size. It doesn't verify internal layer structure or that the architecture matches the flowchart.
- **Suggestion**: Add hidden tests that verify layer types (isinstance checks), parameter counts, or specific intermediate outputs.

#### 6. Problem 5 visible test gives away solution structure
- **Location**: Cell 30 (Problem 5)
- **Description**: The visible test checks `len(data_aug_preprocess.transforms) == 2`, which tells students exactly how many transforms to use.
- **Suggestion**: Make this a hidden test and keep only a basic type check as visible.

#### 7. Inconsistent weight initialization requirements
- **Location**: Problems 3, 4, 6
- **Description**: Problems 3 and 4 specify weight initialization with std=0.05, but Problem 6 doesn't mention it even though it uses ResidualBlock which has its own initialization. This creates ambiguity about whether to initialize the initial conv layer in ResNet18.
- **Suggestion**: Clarify weight initialization requirements for Problem 6, or state that only ResidualBlock layers need custom initialization.

### Minor Issues

- **Cell 3**: The variable `bear_edges` is created but never used. This dead code may confuse students.
- **Cell 8**: The variable name `blurr_kernel` should be `blur_kernel` (misspelling).
- **Cell 11**: The padding rules describe "If padding for rows is odd" but this is slightly confusing since padding is described as a 2-tuple for (rows, columns). Consider rewording for clarity.
- **Cell 23**: The markdown says "60,000 color images" for CIFAR-10, which is correct for total dataset but the actual split is 50,000 train / 10,000 test. The text could be more precise.
- **Cell 32**: The `blocks` attribute is created but registered as a plain Python list, not as `nn.ModuleList`. This means the ResidualBlocks' parameters may not be properly registered with the model. This could cause issues during training.

### Strengths

1. **Progressive difficulty**: The assignment builds from basic convolution implementation to full ResNet18, scaffolding learning effectively.
2. **Visual demonstrations**: The bear image examples help students visualize what convolution does (edge detection, blurring).
3. **Good use of worked examples**: The `ExampleBlock` before Problem 3 demonstrates how to structure nn.Module subclasses.
4. **Comprehensive coverage**: The assignment covers convolution fundamentals, padding/stride, building blocks, skip connections, data augmentation, and a complete modern architecture.
5. **Clear test structure**: Test cells follow the required format with visible assertions, error messages, and hidden tests.
6. **Practical application**: Training on CIFAR-10 gives students experience with a real dataset and realistic training loops.

### Recommendations

**Top 3 Priority Fixes:**

1. **Fix the missing `requests` import** - This is a blocking issue that prevents the notebook from running.

2. **Add text descriptions for all flowchart architectures** - Even if the images work, text descriptions serve as a reference and accessibility fallback. For each architecture:
   - Problem 3: Describe the layer sequence, filter counts, and how the two branches merge
   - Problem 4: Describe both self_conv=True and self_conv=False paths clearly
   - Problem 6: Provide a table or bullet list of all 18 convolutional layers

3. **Make training code device-agnostic** - Replace hardcoded `.cuda()` calls with proper device handling to support students without GPU access.

---
