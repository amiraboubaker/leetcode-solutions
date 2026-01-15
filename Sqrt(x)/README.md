# Intuition
The square root of `x` is the largest integer `k` such that `k * k <= x`.  
Since the answer lies between `0` and `x`, and the condition is monotonic, binary search is the fastest sensible approach.

# Approach
Use binary search between `0` and `x`.  
At each step, compute `mid * mid`:
- If it equals `x`, return `mid`.
- If it is smaller than `x`, move right.
- If it is larger than `x`, move left.  
When the search ends, the right pointer will hold the integer square root.

# Complexity
- Time complexity:  
  O(log x)

- Space complexity:  
  O(1)

# Code
```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 0, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
 
```