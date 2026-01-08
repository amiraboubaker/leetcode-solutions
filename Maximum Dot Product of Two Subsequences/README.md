# 1458. Maximum Dot Product of Two Subsequences

**Solved**  
**Medium**  
**Topics** Array, Dynamic Programming  
**Companies**

## Problem Description

Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

## Intuition
This problem asks for the maximum dot product of subsequences of the same length. 
We need to consider **every pair of elements** from nums1 and nums2 and decide whether to include them in the subsequence or skip them. 
Dynamic programming fits perfectly here.

## Approach
- Let `dp[i][j]` be the **maximum dot product** using `nums1[i:]` and `nums2[j:]`.  
- For each pair `(i, j)`, we have three choices:
  1. Take `nums1[i] * nums2[j]` and add it to `dp[i+1][j+1]` (both elements included in subsequence)
  2. Skip `nums1[i]` → `dp[i+1][j]`
  3. Skip `nums2[j]` → `dp[i][j+1]`
- Take the maximum of these three options.
- Base case: if either array is exhausted, return negative infinity (to avoid empty subsequences).

This ensures we explore all subsequence pairs and pick the one with the maximum dot product.

## Complexity
- Time complexity: O(m × n), where m = len(nums1), n = len(nums2)
- Space complexity: O(m × n) for the DP table

## Examples

### Example 1:

**Input:** nums1 = [2,1,-2,5], nums2 = [3,0,-6]  
**Output:** 18  
**Explanation:** Pick nums1[0], nums1[2], nums1[3] and nums2[0], nums2[2].  
(2*3 + (-2)*(-6) + 5*0) = 6 + 12 + 0 = 18

### Example 2:

**Input:** nums1 = [3,-2], nums2 = [2,-6,7]  
**Output:** 21  
**Explanation:** Pick nums1[0] and nums2[2]. 3*7 = 21

### Example 3:

**Input:** nums1 = [-1,-1], nums2 = [1,1]  
**Output:** -1  
**Explanation:** Pick one from each. -1*1 = -1

## Constraints

- 1 <= nums1.length, nums2.length <= 500
- -1000 <= nums1[i], nums2[i] <= 1000