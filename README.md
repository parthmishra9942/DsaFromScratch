<div align="center">

# ⚔️ Data Structures & Algorithmic Patterns From Scratch
### *Production-Grade Problem Solving, Time-Space Complexity Mastery & FAANG Interview Architecture*

[![LeetCode Profile](https://img.shields.io/badge/LeetCode-parth213g-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/parth213g/)
[![Problems Solved](https://img.shields.io/badge/Problems_Solved-131%2B-00b8a3?style=for-the-badge&logo=hackerrank&logoColor=white)](#-problem-distribution)
[![Portfolio](https://img.shields.io/badge/Live_Portfolio-parthh.runs--on.dev-0284c7?style=for-the-badge&logo=googlechrome&logoColor=white)](https://parthh.runs-on.dev)
[![Author](https://img.shields.io/badge/Author-Parth_Mishra-red?style=for-the-badge&logo=github&logoColor=white)](https://github.com/parthmishra9942)

<p align="center">
  <b>Curated repository of algorithmic solutions, low-level data structure implementations, and pattern-based mental models engineered for Tier-1 technical evaluations (Google, Amazon, Microsoft, Uber, High-Frequency Trading).</b>
</p>

</div>

---

## 📊 Problem Distribution & Difficulty Breakdown

```
        ┌────────────────────────────────────────────────────────┐
        │                 TOTAL SOLVED: 131+                     │
        └───────────────────────────┬────────────────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
 🟢 59 Easy (45.0%)      🟡 58 Medium (44.3%)     🔴 14 Hard (10.7%)
   [Core Foundations]      [System Building Blocks] [Optimal Mathematical Limits]
```

| Difficulty | Count | Primary Algorithmic Focus | Optimal Time Bound |
| :--- | :--- | :--- | :--- |
| **🟢 Easy** | `59` | Fast Two Pointers, HashMap Lookups, In-Place Array Mutation, Tree Traversals | $\mathcal{O}(N)$ / $\mathcal{O}(1)$ Aux |
| **🟡 Medium** | `58` | Monotonic Stacks, Sliding Window with Deques, 0/1 Knapsack DP, Graph BFS/DFS | $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ |
| **🔴 Hard** | `14` | Segment Trees, Multi-Dimensional State Compression DP, Monotonic Deque Optimization | $\mathcal{O}(N \log K)$ or $\mathcal{O}(N)$ |

---

## 🧠 Master Algorithmic Pattern Taxonomy

The core philosophy of this repository: **Do not memorize code—recognize the invariants.**

| # | Algorithmic Pattern | Identifying Trigger / Invariant | Core Data Structure | Canonical Problems Solved |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Two Pointers (Bidirectional & Fast/Slow)** | Sorted contiguous arrays, cycle detection, pair sums | Arrays, Linked Lists | `0015-3sum`, `0016-3sum-closest`, `0018-4sum`, `0141-linked-list-cycle` |
| **2** | **Sliding Window (Dynamic & Fixed)** | Longest/shortest subsegment satisfying dynamic condition $\mathcal{K}$ | Hash Map, Doubly Linked Deque | `0003-longest-substring-without-repeating`, `0209-min-size-subarray`, `0904-fruit-baskets` |
| **3** | **Monotonic Stack & Queue** | Next Greater / Previous Smaller element in $\mathcal{O}(N)$ single pass | LIFO Stack, Monotonic Deque | `0020-valid-parentheses`, `0503-next-greater-ii`, `0739-daily-temperatures` |
| **4** | **Kadane's & Dynamic Invariants** | Maximum subarray sum with at most $k$ deletions / resets | In-Place Prefix Accumulators | `0053-maximum-subarray`, `0152-max-product-subarray`, `0918-circular-subarray` |
| **5** | **Interval Scheduling & Sweep-Line** | Overlapping timelines, interval merging, collision detection | Array Sort + Min-Heap | `0056-merge-intervals`, `0057-insert-interval`, `0986-interval-intersections` |
| **6** | **Prefix Sums & Remainder Hashing** | Subarray sums divisible by $k$ or equal to target $T$ in $\mathcal{O}(1)$ | Hash Table | `0974-subarray-sums-divisible-by-k`, `1749-max-absolute-subarray-sum` |
| **7** | **Tree Depth-First & Breadth-First** | Subtree properties, height balance, level-order invariants | Recursive Call Stack, Queue | `0100-same-tree`, `0110-balanced-binary-tree`, `2265-nodes-equal-to-average` |
| **8** | **Dynamic Programming & State Machines** | Optimal substructure with overlapping subproblems | Memoized Tables, Space-Optimized Rollers | `0070-climbing-stairs`, `0115-distinct-subsequences`, `1140-stone-game-ii` |

---

## ⚡ Big-O Time & Space Reference Matrix

```
Complexity   Class           Description                       Example in Repository
────────────────────────────────────────────────────────────────────────────────────
O(1)         Constant        Hash lookups, bitwise bitmasking   0136-single-number
O(log N)     Logarithmic     Binary Search, Divide & Conquer    0035-search-insert-position
O(N)         Linear          Two Pointers, Monotonic Stack      0739-daily-temperatures
O(N log N)   Linearithmic    Merge Sort, Heap Top-K             0056-merge-intervals
O(N * K)     Pseudo-Linear   Dynamic Programming State Knapsack 0115-distinct-subsequences
O(2^N)       Exponential     Combinatorial Backtracking         0022-generate-parentheses
```

---


<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0001-two-sum) |
| [0014-longest-common-prefix](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0014-longest-common-prefix) |
| [0015-3sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0015-3sum) |
| [0016-3sum-closest](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0016-3sum-closest) |
| [0018-4sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0018-4sum) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0027-remove-element](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0027-remove-element) |
| [0031-next-permutation](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0031-next-permutation) |
| [0035-search-insert-position](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0035-search-insert-position) |
| [0053-maximum-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0053-maximum-subarray) |
| [0056-merge-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0056-merge-intervals) |
| [0057-insert-interval](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0057-insert-interval) |
| [0066-plus-one](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0066-plus-one) |
| [0073-set-matrix-zeroes](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0073-set-matrix-zeroes) |
| [0075-sort-colors](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0075-sort-colors) |
| [0088-merge-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0088-merge-sorted-array) |
| [0136-single-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0136-single-number) |
| [0152-maximum-product-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0152-maximum-product-subarray) |
| [0189-rotate-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0189-rotate-array) |
| [0209-minimum-size-subarray-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0209-minimum-size-subarray-sum) |
| [0219-contains-duplicate-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0219-contains-duplicate-ii) |
| [0228-summary-ranges](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0228-summary-ranges) |
| [0268-missing-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0268-missing-number) |
| [0287-find-the-duplicate-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0287-find-the-duplicate-number) |
| [0503-next-greater-element-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0503-next-greater-element-ii) |
| [0739-daily-temperatures](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0739-daily-temperatures) |
| [0748-shortest-completing-word](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0748-shortest-completing-word) |
| [0904-fruit-into-baskets](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0904-fruit-into-baskets) |
| [0918-maximum-sum-circular-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0918-maximum-sum-circular-subarray) |
| [0974-subarray-sums-divisible-by-k](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0974-subarray-sums-divisible-by-k) |
| [0977-squares-of-a-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0977-squares-of-a-sorted-array) |
| [0986-interval-list-intersections](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0986-interval-list-intersections) |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1186-maximum-subarray-sum-with-one-deletion](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1186-maximum-subarray-sum-with-one-deletion) |
| [1464-maximum-product-of-two-elements-in-an-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1464-maximum-product-of-two-elements-in-an-array) |
| [1477-find-two-non-overlapping-sub-arrays-each-with-target-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum) |
| [1550-three-consecutive-odds](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1550-three-consecutive-odds) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [1658-minimum-operations-to-reduce-x-to-zero](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1658-minimum-operations-to-reduce-x-to-zero) |
| [1749-maximum-absolute-sum-of-any-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1749-maximum-absolute-sum-of-any-subarray) |
| [1807-evaluate-the-bracket-pairs-of-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1807-evaluate-the-bracket-pairs-of-a-string) |
| [2089-find-target-indices-after-sorting-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2089-find-target-indices-after-sorting-array) |
| [2091-removing-minimum-and-maximum-from-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2091-removing-minimum-and-maximum-from-array) |
| [2333-minimum-sum-of-squared-difference](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2333-minimum-sum-of-squared-difference) |
| [2778-sum-of-squares-of-special-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2778-sum-of-squares-of-special-elements) |
| [2897-apply-operations-on-array-to-maximize-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2897-apply-operations-on-array-to-maximize-sum-of-squares) |
| [2913-subarrays-distinct-element-sum-of-squares-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2913-subarrays-distinct-element-sum-of-squares-i) |
| [2916-subarrays-distinct-element-sum-of-squares-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2916-subarrays-distinct-element-sum-of-squares-ii) |
| [2948-make-lexicographically-smallest-array-by-swapping-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2948-make-lexicographically-smallest-array-by-swapping-elements) |
| [3414-maximum-score-of-non-overlapping-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3414-maximum-score-of-non-overlapping-intervals) |
| [3471-find-the-largest-almost-missing-integer](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3471-find-the-largest-almost-missing-integer) |
| [3483-unique-3-digit-even-numbers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3483-unique-3-digit-even-numbers) |
| [3524-find-x-value-of-array-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3524-find-x-value-of-array-i) |
| [3550-smallest-index-with-digit-sum-equal-to-index](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3550-smallest-index-with-digit-sum-equal-to-index) |
| [3568-minimum-moves-to-clean-the-classroom](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3568-minimum-moves-to-clean-the-classroom) |
| [3644-maximum-k-to-sort-a-permutation](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3644-maximum-k-to-sort-a-permutation) |
| [3727-maximum-alternating-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3727-maximum-alternating-sum-of-squares) |
| [3731-find-missing-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3731-find-missing-elements) |
| [3886-sum-of-sortable-integers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3886-sum-of-sortable-integers) |
| [3903-smallest-stable-index-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3903-smallest-stable-index-i) |
| [3904-smallest-stable-index-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3904-smallest-stable-index-ii) |
## Two Pointers
|  |
| ------- |
| [0015-3sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0015-3sum) |
| [0016-3sum-closest](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0016-3sum-closest) |
| [0018-4sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0018-4sum) |
| [0019-remove-nth-node-from-end-of-list](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0027-remove-element](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0027-remove-element) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0031-next-permutation](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0031-next-permutation) |
| [0075-sort-colors](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0075-sort-colors) |
| [0082-remove-duplicates-from-sorted-list-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0082-remove-duplicates-from-sorted-list-ii) |
| [0088-merge-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0088-merge-sorted-array) |
| [0125-valid-palindrome](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0125-valid-palindrome) |
| [0141-linked-list-cycle](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0141-linked-list-cycle) |
| [0189-rotate-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0189-rotate-array) |
| [0202-happy-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0202-happy-number) |
| [0287-find-the-duplicate-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0287-find-the-duplicate-number) |
| [0977-squares-of-a-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0977-squares-of-a-sorted-array) |
| [0986-interval-list-intersections](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0986-interval-list-intersections) |
| [2472-maximum-number-of-non-overlapping-palindrome-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2472-maximum-number-of-non-overlapping-palindrome-substrings) |
| [3302-find-the-lexicographically-smallest-valid-sequence](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3302-find-the-lexicographically-smallest-valid-sequence) |
| [3734-lexicographically-smallest-palindromic-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3734-lexicographically-smallest-palindromic-permutation-greater-than-target) |
## Sorting
|  |
| ------- |
| [0015-3sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0015-3sum) |
| [0016-3sum-closest](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0016-3sum-closest) |
| [0018-4sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0018-4sum) |
| [0056-merge-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0056-merge-intervals) |
| [0075-sort-colors](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0075-sort-colors) |
| [0088-merge-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0088-merge-sorted-array) |
| [0242-valid-anagram](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0242-valid-anagram) |
| [0268-missing-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0268-missing-number) |
| [0977-squares-of-a-sorted-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0977-squares-of-a-sorted-array) |
| [1096-brace-expansion-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1096-brace-expansion-ii) |
| [1464-maximum-product-of-two-elements-in-an-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1464-maximum-product-of-two-elements-in-an-array) |
| [1520-maximum-number-of-non-overlapping-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1520-maximum-number-of-non-overlapping-substrings) |
| [2089-find-target-indices-after-sorting-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2089-find-target-indices-after-sorting-array) |
| [2333-minimum-sum-of-squared-difference](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2333-minimum-sum-of-squared-difference) |
| [2948-make-lexicographically-smallest-array-by-swapping-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2948-make-lexicographically-smallest-array-by-swapping-elements) |
| [3414-maximum-score-of-non-overlapping-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3414-maximum-score-of-non-overlapping-intervals) |
| [3727-maximum-alternating-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3727-maximum-alternating-sum-of-squares) |
| [3731-find-missing-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3731-find-missing-elements) |
| [3886-sum-of-sortable-integers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3886-sum-of-sortable-integers) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0001-two-sum) |
| [0003-longest-substring-without-repeating-characters](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0003-longest-substring-without-repeating-characters) |
| [0073-set-matrix-zeroes](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0073-set-matrix-zeroes) |
| [0141-linked-list-cycle](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0141-linked-list-cycle) |
| [0202-happy-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0202-happy-number) |
| [0219-contains-duplicate-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0219-contains-duplicate-ii) |
| [0242-valid-anagram](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0242-valid-anagram) |
| [0268-missing-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0268-missing-number) |
| [0383-ransom-note](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0383-ransom-note) |
| [0387-first-unique-character-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0387-first-unique-character-in-a-string) |
| [0424-longest-repeating-character-replacement](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0424-longest-repeating-character-replacement) |
| [0748-shortest-completing-word](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0748-shortest-completing-word) |
| [0904-fruit-into-baskets](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0904-fruit-into-baskets) |
| [0974-subarray-sums-divisible-by-k](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0974-subarray-sums-divisible-by-k) |
| [1096-brace-expansion-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1096-brace-expansion-ii) |
| [1189-maximum-number-of-balloons](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1189-maximum-number-of-balloons) |
| [1477-find-two-non-overlapping-sub-arrays-each-with-target-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum) |
| [1520-maximum-number-of-non-overlapping-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1520-maximum-number-of-non-overlapping-substrings) |
| [1658-minimum-operations-to-reduce-x-to-zero](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1658-minimum-operations-to-reduce-x-to-zero) |
| [1807-evaluate-the-bracket-pairs-of-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1807-evaluate-the-bracket-pairs-of-a-string) |
| [2897-apply-operations-on-array-to-maximize-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2897-apply-operations-on-array-to-maximize-sum-of-squares) |
| [2913-subarrays-distinct-element-sum-of-squares-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2913-subarrays-distinct-element-sum-of-squares-i) |
| [2916-subarrays-distinct-element-sum-of-squares-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2916-subarrays-distinct-element-sum-of-squares-ii) |
| [3471-find-the-largest-almost-missing-integer](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3471-find-the-largest-almost-missing-integer) |
| [3483-unique-3-digit-even-numbers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3483-unique-3-digit-even-numbers) |
| [3568-minimum-moves-to-clean-the-classroom](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3568-minimum-moves-to-clean-the-classroom) |
| [3720-lexicographically-smallest-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3720-lexicographically-smallest-permutation-greater-than-target) |
| [3731-find-missing-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3731-find-missing-elements) |
## Math
|  |
| ------- |
| [0009-palindrome-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0009-palindrome-number) |
| [0029-divide-two-integers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0029-divide-two-integers) |
| [0066-plus-one](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0066-plus-one) |
| [0069-sqrtx](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0069-sqrtx) |
| [0070-climbing-stairs](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0070-climbing-stairs) |
| [0172-factorial-trailing-zeroes](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0172-factorial-trailing-zeroes) |
| [0189-rotate-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0189-rotate-array) |
| [0202-happy-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0202-happy-number) |
| [0231-power-of-two](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0231-power-of-two) |
| [0258-add-digits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0258-add-digits) |
| [0263-ugly-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0263-ugly-number) |
| [0268-missing-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0268-missing-number) |
| [0412-fizz-buzz](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0412-fizz-buzz) |
| [0415-add-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0415-add-strings) |
| [0509-fibonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0509-fibonacci-number) |
| [0836-rectangle-overlap](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0836-rectangle-overlap) |
| [1071-greatest-common-divisor-of-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1071-greatest-common-divisor-of-strings) |
| [1137-n-th-tribonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1137-n-th-tribonacci-number) |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1401-circle-and-rectangle-overlapping](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1401-circle-and-rectangle-overlapping) |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
| [1518-water-bottles](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1518-water-bottles) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [1621-number-of-sets-of-k-non-overlapping-line-segments](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1621-number-of-sets-of-k-non-overlapping-line-segments) |
| [2409-count-days-spent-together](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2409-count-days-spent-together) |
| [2769-find-the-maximum-achievable-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2769-find-the-maximum-achievable-number) |
| [3345-smallest-divisible-digit-product-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3345-smallest-divisible-digit-product-i) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3348-smallest-divisible-digit-product-ii) |
| [3524-find-x-value-of-array-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3524-find-x-value-of-array-i) |
| [3550-smallest-index-with-digit-sum-equal-to-index](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3550-smallest-index-with-digit-sum-equal-to-index) |
| [3723-maximize-sum-of-squares-of-digits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3723-maximize-sum-of-squares-of-digits) |
| [3756-concatenate-non-zero-digits-and-multiply-by-sum-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii) |
| [3870-count-commas-in-range](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3870-count-commas-in-range) |
| [3871-count-commas-in-range-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3871-count-commas-in-range-ii) |
| [3886-sum-of-sortable-integers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3886-sum-of-sortable-integers) |
## Bit Manipulation
|  |
| ------- |
| [0029-divide-two-integers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0029-divide-two-integers) |
| [0136-single-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0136-single-number) |
| [0190-reverse-bits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0190-reverse-bits) |
| [0231-power-of-two](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0231-power-of-two) |
| [0268-missing-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0268-missing-number) |
| [0287-find-the-duplicate-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0287-find-the-duplicate-number) |
| [2897-apply-operations-on-array-to-maximize-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2897-apply-operations-on-array-to-maximize-sum-of-squares) |
| [3568-minimum-moves-to-clean-the-classroom](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3568-minimum-moves-to-clean-the-classroom) |
| [3644-maximum-k-to-sort-a-permutation](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3644-maximum-k-to-sort-a-permutation) |
## Recursion
|  |
| ------- |
| [0021-merge-two-sorted-lists](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0021-merge-two-sorted-lists) |
| [0024-swap-nodes-in-pairs](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0024-swap-nodes-in-pairs) |
| [0231-power-of-two](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0231-power-of-two) |
| [0509-fibonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0509-fibonacci-number) |
| [3483-unique-3-digit-even-numbers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3483-unique-3-digit-even-numbers) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0003-longest-substring-without-repeating-characters) |
| [0014-longest-common-prefix](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0014-longest-common-prefix) |
| [0020-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0020-valid-parentheses) |
| [0022-generate-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0022-generate-parentheses) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0032-longest-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0032-longest-valid-parentheses) |
| [0038-count-and-say](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0038-count-and-say) |
| [0058-length-of-last-word](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0058-length-of-last-word) |
| [0093-restore-ip-addresses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0093-restore-ip-addresses) |
| [0097-interleaving-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0097-interleaving-string) |
| [0115-distinct-subsequences](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0115-distinct-subsequences) |
| [0125-valid-palindrome](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0125-valid-palindrome) |
| [0242-valid-anagram](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0242-valid-anagram) |
| [0301-remove-invalid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0301-remove-invalid-parentheses) |
| [0383-ransom-note](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0383-ransom-note) |
| [0387-first-unique-character-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0387-first-unique-character-in-a-string) |
| [0412-fizz-buzz](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0412-fizz-buzz) |
| [0415-add-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0415-add-strings) |
| [0424-longest-repeating-character-replacement](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0424-longest-repeating-character-replacement) |
| [0748-shortest-completing-word](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0748-shortest-completing-word) |
| [0856-score-of-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0856-score-of-parentheses) |
| [0921-minimum-add-to-make-parentheses-valid](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0921-minimum-add-to-make-parentheses-valid) |
| [0940-distinct-subsequences-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0940-distinct-subsequences-ii) |
| [1021-remove-outermost-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1021-remove-outermost-parentheses) |
| [1047-remove-all-adjacent-duplicates-in-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1047-remove-all-adjacent-duplicates-in-string) |
| [1071-greatest-common-divisor-of-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1071-greatest-common-divisor-of-strings) |
| [1096-brace-expansion-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1096-brace-expansion-ii) |
| [1111-maximum-nesting-depth-of-two-valid-parentheses-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1111-maximum-nesting-depth-of-two-valid-parentheses-strings) |
| [1189-maximum-number-of-balloons](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1189-maximum-number-of-balloons) |
| [1190-reverse-substrings-between-each-pair-of-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1190-reverse-substrings-between-each-pair-of-parentheses) |
| [1209-remove-all-adjacent-duplicates-in-string-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1209-remove-all-adjacent-duplicates-in-string-ii) |
| [1520-maximum-number-of-non-overlapping-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1520-maximum-number-of-non-overlapping-substrings) |
| [1541-minimum-insertions-to-balance-a-parentheses-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1541-minimum-insertions-to-balance-a-parentheses-string) |
| [1807-evaluate-the-bracket-pairs-of-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1807-evaluate-the-bracket-pairs-of-a-string) |
| [2409-count-days-spent-together](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2409-count-days-spent-together) |
| [2472-maximum-number-of-non-overlapping-palindrome-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2472-maximum-number-of-non-overlapping-palindrome-substrings) |
| [3302-find-the-lexicographically-smallest-valid-sequence](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3302-find-the-lexicographically-smallest-valid-sequence) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3348-smallest-divisible-digit-product-ii) |
| [3498-reverse-degree-of-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3498-reverse-degree-of-a-string) |
| [3720-lexicographically-smallest-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3720-lexicographically-smallest-permutation-greater-than-target) |
| [3734-lexicographically-smallest-palindromic-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3734-lexicographically-smallest-palindromic-permutation-greater-than-target) |
| [3756-concatenate-non-zero-digits-and-multiply-by-sum-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii) |
| [3798-largest-even-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3798-largest-even-number) |
| [3863-minimum-operations-to-sort-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3863-minimum-operations-to-sort-a-string) |
## Simulation
|  |
| ------- |
| [0258-add-digits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0258-add-digits) |
| [0412-fizz-buzz](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0412-fizz-buzz) |
| [0415-add-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0415-add-strings) |
| [1518-water-bottles](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1518-water-bottles) |
| [3498-reverse-degree-of-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3498-reverse-degree-of-a-string) |
## Binary Search
|  |
| ------- |
| [0035-search-insert-position](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0035-search-insert-position) |
| [0069-sqrtx](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0069-sqrtx) |
| [0209-minimum-size-subarray-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0209-minimum-size-subarray-sum) |
| [0268-missing-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0268-missing-number) |
| [0287-find-the-duplicate-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0287-find-the-duplicate-number) |
| [1477-find-two-non-overlapping-sub-arrays-each-with-target-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum) |
| [1658-minimum-operations-to-reduce-x-to-zero](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1658-minimum-operations-to-reduce-x-to-zero) |
| [2089-find-target-indices-after-sorting-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2089-find-target-indices-after-sorting-array) |
| [2333-minimum-sum-of-squared-difference](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2333-minimum-sum-of-squared-difference) |
| [3414-maximum-score-of-non-overlapping-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3414-maximum-score-of-non-overlapping-intervals) |
## Dynamic Programming
|  |
| ------- |
| [0022-generate-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0022-generate-parentheses) |
| [0032-longest-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0032-longest-valid-parentheses) |
| [0053-maximum-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0053-maximum-subarray) |
| [0070-climbing-stairs](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0070-climbing-stairs) |
| [0097-interleaving-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0097-interleaving-string) |
| [0115-distinct-subsequences](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0115-distinct-subsequences) |
| [0152-maximum-product-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0152-maximum-product-subarray) |
| [0509-fibonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0509-fibonacci-number) |
| [0918-maximum-sum-circular-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0918-maximum-sum-circular-subarray) |
| [0940-distinct-subsequences-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0940-distinct-subsequences-ii) |
| [1137-n-th-tribonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1137-n-th-tribonacci-number) |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1186-maximum-subarray-sum-with-one-deletion](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1186-maximum-subarray-sum-with-one-deletion) |
| [1477-find-two-non-overlapping-sub-arrays-each-with-target-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum) |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [1621-number-of-sets-of-k-non-overlapping-line-segments](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1621-number-of-sets-of-k-non-overlapping-line-segments) |
| [1749-maximum-absolute-sum-of-any-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1749-maximum-absolute-sum-of-any-subarray) |
| [2472-maximum-number-of-non-overlapping-palindrome-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2472-maximum-number-of-non-overlapping-palindrome-substrings) |
| [3302-find-the-lexicographically-smallest-valid-sequence](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3302-find-the-lexicographically-smallest-valid-sequence) |
| [3414-maximum-score-of-non-overlapping-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3414-maximum-score-of-non-overlapping-intervals) |
| [3524-find-x-value-of-array-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3524-find-x-value-of-array-i) |
## Memoization
|  |
| ------- |
| [0070-climbing-stairs](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0070-climbing-stairs) |
| [0509-fibonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0509-fibonacci-number) |
| [1137-n-th-tribonacci-number](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1137-n-th-tribonacci-number) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
## Heap (Priority Queue)
|  |
| ------- |
| [1464-maximum-product-of-two-elements-in-an-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1464-maximum-product-of-two-elements-in-an-array) |
| [2333-minimum-sum-of-squared-difference](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2333-minimum-sum-of-squared-difference) |
## Backtracking
|  |
| ------- |
| [0022-generate-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0022-generate-parentheses) |
| [0093-restore-ip-addresses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0093-restore-ip-addresses) |
| [0301-remove-invalid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0301-remove-invalid-parentheses) |
| [1096-brace-expansion-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1096-brace-expansion-ii) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3348-smallest-divisible-digit-product-ii) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0003-longest-substring-without-repeating-characters) |
| [0209-minimum-size-subarray-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0209-minimum-size-subarray-sum) |
| [0219-contains-duplicate-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0219-contains-duplicate-ii) |
| [0424-longest-repeating-character-replacement](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0424-longest-repeating-character-replacement) |
| [0904-fruit-into-baskets](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0904-fruit-into-baskets) |
| [1477-find-two-non-overlapping-sub-arrays-each-with-target-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum) |
| [1658-minimum-operations-to-reduce-x-to-zero](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1658-minimum-operations-to-reduce-x-to-zero) |
## Prefix Sum
|  |
| ------- |
| [0209-minimum-size-subarray-sum](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0209-minimum-size-subarray-sum) |
| [0974-subarray-sums-divisible-by-k](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0974-subarray-sums-divisible-by-k) |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1621-number-of-sets-of-k-non-overlapping-line-segments](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1621-number-of-sets-of-k-non-overlapping-line-segments) |
| [1658-minimum-operations-to-reduce-x-to-zero](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1658-minimum-operations-to-reduce-x-to-zero) |
| [3756-concatenate-non-zero-digits-and-multiply-by-sum-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii) |
| [3903-smallest-stable-index-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3903-smallest-stable-index-i) |
| [3904-smallest-stable-index-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3904-smallest-stable-index-ii) |
## Number Theory
|  |
| ------- |
| [0258-add-digits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0258-add-digits) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3348-smallest-divisible-digit-product-ii) |
## String Matching
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Linked List
|  |
| ------- |
| [0019-remove-nth-node-from-end-of-list](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0021-merge-two-sorted-lists](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0021-merge-two-sorted-lists) |
| [0024-swap-nodes-in-pairs](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0024-swap-nodes-in-pairs) |
| [0082-remove-duplicates-from-sorted-list-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0082-remove-duplicates-from-sorted-list-ii) |
| [0083-remove-duplicates-from-sorted-list](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0083-remove-duplicates-from-sorted-list) |
| [0141-linked-list-cycle](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0141-linked-list-cycle) |
| [2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points) |
## Trie
|  |
| ------- |
| [0014-longest-common-prefix](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0014-longest-common-prefix) |
## Divide and Conquer
|  |
| ------- |
| [0053-maximum-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0053-maximum-subarray) |
| [0190-reverse-bits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0190-reverse-bits) |
| [0918-maximum-sum-circular-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0918-maximum-sum-circular-subarray) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
## Queue
|  |
| ------- |
| [0387-first-unique-character-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0387-first-unique-character-in-a-string) |
| [0918-maximum-sum-circular-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0918-maximum-sum-circular-subarray) |
## Monotonic Queue
|  |
| ------- |
| [0918-maximum-sum-circular-subarray](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0918-maximum-sum-circular-subarray) |
## Depth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0100-same-tree) |
| [0110-balanced-binary-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0110-balanced-binary-tree) |
| [2265-count-nodes-equal-to-average-of-subtree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2265-count-nodes-equal-to-average-of-subtree) |
| [3310-remove-methods-from-project](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3310-remove-methods-from-project) |
## Breadth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0100-same-tree) |
| [0301-remove-invalid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0301-remove-invalid-parentheses) |
| [1096-brace-expansion-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1096-brace-expansion-ii) |
| [3310-remove-methods-from-project](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3310-remove-methods-from-project) |
| [3568-minimum-moves-to-clean-the-classroom](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3568-minimum-moves-to-clean-the-classroom) |
## Graph Theory
|  |
| ------- |
| [3310-remove-methods-from-project](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3310-remove-methods-from-project) |
## Enumeration
|  |
| ------- |
| [2778-sum-of-squares-of-special-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2778-sum-of-squares-of-special-elements) |
| [3345-smallest-divisible-digit-product-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3345-smallest-divisible-digit-product-i) |
| [3483-unique-3-digit-even-numbers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3483-unique-3-digit-even-numbers) |
| [3720-lexicographically-smallest-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3720-lexicographically-smallest-permutation-greater-than-target) |
| [3734-lexicographically-smallest-palindromic-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3734-lexicographically-smallest-palindromic-permutation-greater-than-target) |
| [3886-sum-of-sortable-integers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3886-sum-of-sortable-integers) |
## Greedy
|  |
| ------- |
| [0921-minimum-add-to-make-parentheses-valid](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0921-minimum-add-to-make-parentheses-valid) |
| [1520-maximum-number-of-non-overlapping-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1520-maximum-number-of-non-overlapping-substrings) |
| [1541-minimum-insertions-to-balance-a-parentheses-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1541-minimum-insertions-to-balance-a-parentheses-string) |
| [2091-removing-minimum-and-maximum-from-array](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2091-removing-minimum-and-maximum-from-array) |
| [2333-minimum-sum-of-squared-difference](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2333-minimum-sum-of-squared-difference) |
| [2472-maximum-number-of-non-overlapping-palindrome-substrings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2472-maximum-number-of-non-overlapping-palindrome-substrings) |
| [2897-apply-operations-on-array-to-maximize-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2897-apply-operations-on-array-to-maximize-sum-of-squares) |
| [3302-find-the-lexicographically-smallest-valid-sequence](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3302-find-the-lexicographically-smallest-valid-sequence) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3348-smallest-divisible-digit-product-ii) |
| [3720-lexicographically-smallest-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3720-lexicographically-smallest-permutation-greater-than-target) |
| [3723-maximize-sum-of-squares-of-digits](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3723-maximize-sum-of-squares-of-digits) |
| [3727-maximum-alternating-sum-of-squares](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3727-maximum-alternating-sum-of-squares) |
## Minimax
|  |
| ------- |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
## Game Theory
|  |
| ------- |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
## Zero-Sum Game
|  |
| ------- |
| [1140-stone-game-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1140-stone-game-ii) |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
## Nim Game
|  |
| ------- |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
## Sprague–Grundy Theorem
|  |
| ------- |
| [1510-stone-game-iv](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1510-stone-game-iv) |
## Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0100-same-tree) |
| [0110-balanced-binary-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0110-balanced-binary-tree) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [2265-count-nodes-equal-to-average-of-subtree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2265-count-nodes-equal-to-average-of-subtree) |
## Binary Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0100-same-tree) |
| [0110-balanced-binary-tree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0110-balanced-binary-tree) |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [2265-count-nodes-equal-to-average-of-subtree](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2265-count-nodes-equal-to-average-of-subtree) |
## Database
|  |
| ------- |
| [0181-employees-earning-more-than-their-managers](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0181-employees-earning-more-than-their-managers) |
| [0196-delete-duplicate-emails](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0196-delete-duplicate-emails) |
| [0197-rising-temperature](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0197-rising-temperature) |
## Quicksort
|  |
| ------- |
| [0056-merge-intervals](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0056-merge-intervals) |
## Matrix
|  |
| ------- |
| [0073-set-matrix-zeroes](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0073-set-matrix-zeroes) |
| [3568-minimum-moves-to-clean-the-classroom](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3568-minimum-moves-to-clean-the-classroom) |
## Geometry
|  |
| ------- |
| [0836-rectangle-overlap](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0836-rectangle-overlap) |
| [1401-circle-and-rectangle-overlapping](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1401-circle-and-rectangle-overlapping) |
## Combinatorics
|  |
| ------- |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [1621-number-of-sets-of-k-non-overlapping-line-segments](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1621-number-of-sets-of-k-non-overlapping-line-segments) |
## Sweep Line
|  |
| ------- |
| [0986-interval-list-intersections](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0986-interval-list-intersections) |
## Stack
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0020-valid-parentheses) |
| [0032-longest-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0032-longest-valid-parentheses) |
| [0503-next-greater-element-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0503-next-greater-element-ii) |
| [0739-daily-temperatures](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0739-daily-temperatures) |
| [0856-score-of-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0856-score-of-parentheses) |
| [0921-minimum-add-to-make-parentheses-valid](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0921-minimum-add-to-make-parentheses-valid) |
| [1021-remove-outermost-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1021-remove-outermost-parentheses) |
| [1047-remove-all-adjacent-duplicates-in-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1047-remove-all-adjacent-duplicates-in-string) |
| [1096-brace-expansion-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1096-brace-expansion-ii) |
| [1111-maximum-nesting-depth-of-two-valid-parentheses-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1111-maximum-nesting-depth-of-two-valid-parentheses-strings) |
| [1190-reverse-substrings-between-each-pair-of-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1190-reverse-substrings-between-each-pair-of-parentheses) |
| [1209-remove-all-adjacent-duplicates-in-string-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1209-remove-all-adjacent-duplicates-in-string-ii) |
| [1541-minimum-insertions-to-balance-a-parentheses-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1541-minimum-insertions-to-balance-a-parentheses-string) |
## Bracket Sequences
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0020-valid-parentheses) |
| [0022-generate-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0022-generate-parentheses) |
| [0032-longest-valid-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0032-longest-valid-parentheses) |
| [0856-score-of-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0856-score-of-parentheses) |
| [0921-minimum-add-to-make-parentheses-valid](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0921-minimum-add-to-make-parentheses-valid) |
| [1021-remove-outermost-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1021-remove-outermost-parentheses) |
| [1111-maximum-nesting-depth-of-two-valid-parentheses-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1111-maximum-nesting-depth-of-two-valid-parentheses-strings) |
| [1190-reverse-substrings-between-each-pair-of-parentheses](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1190-reverse-substrings-between-each-pair-of-parentheses) |
| [1541-minimum-insertions-to-balance-a-parentheses-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1541-minimum-insertions-to-balance-a-parentheses-string) |
## Monotonic Stack
|  |
| ------- |
| [0503-next-greater-element-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0503-next-greater-element-ii) |
| [0739-daily-temperatures](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0739-daily-temperatures) |
## Counting
|  |
| ------- |
| [0383-ransom-note](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0383-ransom-note) |
| [0387-first-unique-character-in-a-string](https://github.com/parthmishra9942/DsaFromScratch/tree/master/0387-first-unique-character-in-a-string) |
| [1189-maximum-number-of-balloons](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1189-maximum-number-of-balloons) |
| [3720-lexicographically-smallest-permutation-greater-than-target](https://github.com/parthmishra9942/DsaFromScratch/tree/master/3720-lexicographically-smallest-permutation-greater-than-target) |
## Euclidean Algorithm
|  |
| ------- |
| [1071-greatest-common-divisor-of-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1071-greatest-common-divisor-of-strings) |
## Greatest Common Divisor
|  |
| ------- |
| [1071-greatest-common-divisor-of-strings](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1071-greatest-common-divisor-of-strings) |
## Binary Indexed Tree
|  |
| ------- |
| [2913-subarrays-distinct-element-sum-of-squares-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2913-subarrays-distinct-element-sum-of-squares-i) |
| [2916-subarrays-distinct-element-sum-of-squares-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2916-subarrays-distinct-element-sum-of-squares-ii) |
## Segment Tree
|  |
| ------- |
| [2913-subarrays-distinct-element-sum-of-squares-i](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2913-subarrays-distinct-element-sum-of-squares-i) |
| [2916-subarrays-distinct-element-sum-of-squares-ii](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2916-subarrays-distinct-element-sum-of-squares-ii) |
## Union-Find
|  |
| ------- |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
| [2948-make-lexicographically-smallest-array-by-swapping-elements](https://github.com/parthmishra9942/DsaFromScratch/tree/master/2948-make-lexicographically-smallest-array-by-swapping-elements) |
## Binary Search Tree
|  |
| ------- |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
## Fermat's Little Theorem
|  |
| ------- |
| [1569-number-of-ways-to-reorder-array-to-get-same-bst](https://github.com/parthmishra9942/DsaFromScratch/tree/master/1569-number-of-ways-to-reorder-array-to-get-same-bst) |
<!---LeetCode Topics End-->


---

<div align="center">
  <sub>Engineered by <b><a href="https://github.com/parthmishra9942">Parth Mishra</a></b> · B.Tech CSE (AI/ML) @ VIT Bhopal · High-Performance Problem Solving</sub>
</div>
