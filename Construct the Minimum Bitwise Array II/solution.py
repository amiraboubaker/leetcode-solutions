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