# Intuition
# Checking every possible square and summing its elements directly would be too slow.
# Using a prefix sum matrix allows computing the sum of any square in constant time.
# Once sums are fast, the problem becomes finding the largest possible square whose sum is less than or equal to the threshold, which naturally leads to binary search on the side length.

# Approach
# 1. Build a prefix sum matrix `ps` where `ps[i][j]` represents the sum of elements from `(0,0)` to `(i-1,j-1)`.
# 2. Define a helper function `exists(k)` that checks whether there exists at least one `k x k` square with sum <= `threshold` using the prefix sums.
# 3. Use binary search on the side length from `0` to `min(m, n)`:
#    - If a square of size `mid` exists, store it as a candidate answer and search for a larger size.
#    - Otherwise, search for a smaller size.
# 4. Return the maximum valid side length found.

# Complexity
# - Time complexity:
#   $$O(m \cdot n \cdot \log(\min(m, n)))$$
# - Space complexity:
#   $$O(m \cdot n)$$

# Code
class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        
        # Build prefix sum matrix
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = (
                    mat[i][j]
                    + ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j]
                )

        # Function to check if a square of size k exists
        def exists(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    square_sum = (
                        ps[i][j]
                        - ps[i - k][j]
                        - ps[i][j - k]
                        + ps[i - k][j - k]
                    )
                    if square_sum <= threshold:
                        return True
            return False

        # Binary search on side length
        left, right, ans = 0, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans