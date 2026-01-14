# Intuition
# 1. A palindrome reads the same forward and backward.
# 2. Negative numbers cannot be palindromes because of the minus sign.
# 3. If reversing the digits of a number gives the same value, the number is a palindrome.

# Approach
# 1. If the number is negative, return false immediately.
# 2. Store the original value of the number.
# 3. Reverse the number digit by digit using modulo and integer division.
# 4. Compare the reversed number with the original value.
# 5. Return the comparison result.

# Complexity
# - Time complexity:
#   1. Each digit is processed once.
#   2. If the number has d digits, the time complexity is O(d).

# - Space complexity:
#   1. Only constant extra variables are used.
#   2. Space complexity is O(1).

# Code
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num