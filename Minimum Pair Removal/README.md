# Intuition
- The problem forces us to always merge the adjacent pair with the smallest sum.
- Since we cannot choose freely, the only solution is to simulate the operations.
- We repeat the process until the array becomes non-decreasing.

# Approach
- Check if the array is already non-decreasing.
- While it is not:
  - Find the adjacent pair with the minimum sum.
  - Merge the pair into one element.
  - Count the operation.
- Return the total number of operations.

# Complexity
- Time complexity:
  - $$O(n^2)$$
- Space complexity:
  - $$O(n)$$

# Code
```python
class Solution(object):
    def minimumPairRemoval(self, nums):
        def is_non_decreasing(arr):
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

        operations = 0

        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            operations += 1

        return operations
```