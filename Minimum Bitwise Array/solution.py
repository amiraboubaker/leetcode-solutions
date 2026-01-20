# Intuition
# The expression `x OR (x + 1)` is always greater than or equal to `x + 1` and is always odd.
# Instead of overthinking bit patterns, we can directly test values of `x` starting from `0`
# and pick the smallest one that satisfies:
# x OR (x + 1) == nums[i]
# The constraints are small, so brute force is completely safe and simpler than clever-but-wrong tricks.

# Approach
# For each number in `nums`:
# 1. Try all values of `x` from `0` to `nums[i]`.
# 2. Check if `x OR (x + 1) == nums[i]`.
# 3. The first valid `x` is the minimum, so store it.
# 4. If no such `x` exists, store `-1`.

# Complexity
# - Time complexity:
#   $$O(n \cdot M)$$ where `M ≤ 1000`
# - Space complexity:
#   $$O(1)$$ (excluding output array)

# Code
class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []

        for num in nums:
            found = -1
            for x in range(num):
                if (x | (x + 1)) == num:
                    found = x
                    break
            ans.append(found)

        return ans