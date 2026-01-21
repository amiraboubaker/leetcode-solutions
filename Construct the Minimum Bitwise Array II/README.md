# 3315. Construct the Minimum Bitwise Array II

## Intuition
We want the smallest value `x` such that `x OR (x + 1) = n`.  
Observing bit behavior, the OR of two consecutive numbers always produces a number that ends with a block of `1`s. Therefore, if `n` is even, it is impossible. Since `n` is prime, only `n = 2` fails.  
For odd `n`, the result depends on the number of trailing `1`s in its binary representation.

## Approach
For each number `n`:
- If `n == 2`, return `-1` because the OR of consecutive numbers is always odd.
- Otherwise, count how many trailing `1` bits `n` has.
- Let this count be `k`. The minimum valid answer is obtained by subtracting `2^(k-1)` from `n`.
This guarantees both correctness and minimality.

## Complexity
- Time complexity:  
  $$O(n \log M)$$ where \(M\) is the maximum value in `nums` (due to bit counting).

- Space complexity:  
  $$O(1)$$ (excluding the output array).

## Code
```python
class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue

            k = 0
            temp = n
            while temp & 1:
                k += 1
                temp >>= 1

            ans.append(n - (1 << (k - 1)))

        return ans
```