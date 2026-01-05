---
## Critique: DATASCI 503, Homework 9: Clustering and Principal Component Analysis

### Summary
- **Critical issues**: 2
- **Moderate issues**: 5
- **Minor issues**: 6

### Critical Issues

#### 1. Incorrect Hidden Test in Problem 1e
**Location**: Cell 17 (test cell for Problem 1e)

**Description**: The hidden test asserts that `linkage_reordered[0, 2]` should match `linkage_complete[0, 2]`. However, when the dissimilarity matrix is reordered, the linkage function produces a linkage matrix with different internal indices and potentially different merge orders.

**Why problematic**: The merge distances will be the same *in aggregate*, but the positions in the linkage matrix may differ because scipy's linkage assigns new cluster indices based on the order of observations. The first merge in the reordered matrix may not correspond to the first merge in the original matrix. This test may fail for correct student solutions.

**Suggested fix**: Either remove this hidden test or compare the set of merge distances rather than specific positions:
```python
# Check that the same merge distances exist (regardless of order)
assert set(np.round(linkage_reordered[:, 2], 2)) == set(np.round(linkage_complete[:, 2], 2)), "Same merge distances should exist"
```

#### 2. Misleading Hint in Problem 1a About scipy.cluster.hierarchy.linkage Input
**Location**: Cell 3 (Problem 1a markdown)

**Description**: The hint says "since we have a full dissimilarity matrix, pass it directly." However, `scipy.cluster.hierarchy.linkage()` does NOT accept a full dissimilarity matrix directly. It expects either:
1. A condensed distance matrix (1D array from `scipy.spatial.distance.squareform`)
2. An observation matrix (2D array where it computes distances)

Passing a full 4x4 matrix directly treats each row as a 4-dimensional observation, not as pairwise distances.

**Why problematic**: The solution code passes `dissimilarity_matrix` directly to `linkage()`, which will produce incorrect clustering results. This fundamentally breaks the entire first question.

**Suggested fix**: Convert to condensed form first:
```python
from scipy.spatial.distance import squareform
condensed = squareform(dissimilarity_matrix)
linkage_complete = linkage(condensed, method="complete")
```
Update the hint accordingly to explain this requirement.

### Moderate Issues

#### 1. Test in Problem 3b Asserts Specific Number of Clusters
**Location**: Cell 32

**Description**: The test asserts `num_clusters == 5` when cutting at `t=75`, but the number of clusters at a given threshold depends on the data and linkage structure. The problem states "Cut the dendrogram at a distance threshold of `t=75` to obtain cluster assignments" but then tests for exactly 5 clusters.

**Suggestion**: Either change the problem to ask students to find the threshold that produces 5 clusters, or update the test to be less rigid:
```python
assert num_clusters >= 2, "Should produce at least 2 clusters"
```

#### 2. Inconsistent Use of 1-Indexed vs 0-Indexed Labels
**Location**: Cells 36-37 (Problem 3c)

**Description**: The solution adds 1 to K-means labels to make them 1-indexed for "consistency with hierarchical," but this is non-standard practice. scikit-learn returns 0-indexed labels, and converting adds unnecessary complexity.

**Suggestion**: Either keep both as 0-indexed (more Pythonic) or explicitly explain in the problem why 1-indexing is being used. The hidden test checking for 1-indexing should also be updated if the convention changes.

#### 3. Missing Documentation Links
**Location**: Throughout

**Description**: The assignment uses several sklearn and scipy functions but doesn't link to their documentation. Given the note in Problem 1a about needing to do this by hand on an exam, more educational scaffolding about how these algorithms work would be valuable.

**Suggestion**: Add links to:
- [scipy.cluster.hierarchy.linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html)
- [sklearn PCA documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [sklearn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

#### 4. Problem 3d Title Says "Effect of Scaling" but No Discussion Question
**Location**: Cell 39 (Problem 3d)

**Description**: The problem asks students to scale data and compare silhouette scores but doesn't require them to interpret or discuss the results. The silhouette score comparison is shown in a non-solution cell, missing an opportunity for reflection.

**Suggestion**: Add a free-response component asking students to explain why scaling affected the results differently for each method, or which approach they would recommend for this dataset.

#### 5. Problem 3e Uses Unscaled Data for PCA
**Location**: Cell 43 (Problem 3e)

**Description**: The problem applies PCA to unscaled data. While this is a valid pedagogical choice (to show how one feature can dominate), it's worth noting that PCA on unscaled data is often misleading. The hidden test even checks that PC1 explains >90% variance, which is expected since Assault has much higher values than other features.

**Suggestion**: Either:
1. Add a follow-up problem doing PCA on scaled data for comparison, or
2. Add a note explaining why this demonstrates the importance of scaling

### Minor Issues

- **Problem header inconsistency**: Some problems use "Problem Na:" while the convention in CLAUDE.md suggests `### Problem N: Title`. The use of "1a", "1b" sub-problems is fine but should be documented.

- **Warnings suppression**: Cell 1 includes `warnings.filterwarnings("ignore")` which hides potentially useful deprecation warnings from students.

- **Magic numbers**: The thresholds `t=75` and `t=3.2` appear without explanation of how they were chosen. Adding a brief note would help students understand parameter selection.

- **Missing `n_init` deprecation note**: In newer sklearn versions, `n_init="auto"` is the default. Specifying `n_init=10` is good practice but could be explained.

- **Problem 2 has no code cells**: While the theory questions are good, adding a cell where students can verify their hand calculations would reinforce learning.

- **No explicit random seed in hierarchical clustering**: While hierarchical clustering is deterministic, adding consistency notes would help students understand reproducibility.

### Strengths

1. **Well-structured progression**: The assignment moves logically from simple dissimilarity matrices to real-world data, and from hierarchical clustering to K-means to PCA.

2. **Good mix of theory and practice**: Question 2 provides valuable theoretical grounding with hand calculations before applying sklearn in Question 3.

3. **Excellent visualization support**: The silhouette plot helper function is well-implemented and provides meaningful feedback for cluster quality evaluation.

4. **Pedagogically sound comparisons**: Comparing single vs. complete linkage, scaled vs. unscaled data, and hierarchical vs. K-means gives students practical insight into method selection.

5. **Good test cell structure**: Most test cells follow the convention with visible assertions, descriptive error messages, and appropriate hidden tests.

6. **Relevant real-world dataset**: The US Arrests dataset is a classic example that students can relate to and interpret meaningfully.

### Recommendations

1. **[Critical] Fix the linkage input issue in Problem 1**: Convert the full dissimilarity matrix to condensed form using `squareform()` before passing to `linkage()`. This is fundamental to the correctness of the entire first question.

2. **[Critical] Fix the hidden test in Problem 1e**: Update to compare the set of merge distances rather than specific positions in the linkage matrix.

3. **[Moderate] Add interpretation/discussion questions**: Include at least one free-response question asking students to interpret results, such as explaining why scaling affects clustering or what the principal components represent semantically.
---
