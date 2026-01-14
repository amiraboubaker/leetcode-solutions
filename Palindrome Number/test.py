from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Positive palindrome
    x1 = 121
    result1 = sol.isPalindrome(x1)
    expected1 = True
    print(f"Test 1: Input: {x1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2: Negative number
    x2 = -121
    result2 = sol.isPalindrome(x2)
    expected2 = False
    print(f"Test 2: Input: {x2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3: Not a palindrome
    x3 = 10
    result3 = sol.isPalindrome(x3)
    expected3 = False
    print(f"Test 3: Input: {x3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")
    
    # Test Case 4: Single digit (palindrome)
    x4 = 0
    result4 = sol.isPalindrome(x4)
    expected4 = True
    print(f"Test 4: Input: {x4}, Output: {result4}, Expected: {expected4} - {'Accepted' if result4 == expected4 else 'Failed'}")