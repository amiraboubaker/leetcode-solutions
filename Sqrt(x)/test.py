from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    x1 = 4
    result1 = sol.mySqrt(x1)
    expected1 = 2
    print(f"Test 1: Input: {x1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    x2 = 8
    result2 = sol.mySqrt(x2)
    expected2 = 2
    print(f"Test 2: Input: {x2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3
    x3 = 9
    result3 = sol.mySqrt(x3)
    expected3 = 3
    print(f"Test 3: Input: {x3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")
    
    # Test Case 4
    x4 = 0
    result4 = sol.mySqrt(x4)
    expected4 = 0
    print(f"Test 4: Input: {x4}, Output: {result4}, Expected: {expected4} - {'Accepted' if result4 == expected4 else 'Failed'}")
    
    # Test Case 5
    x5 = 1
    result5 = sol.mySqrt(x5)
    expected5 = 1
    print(f"Test 5: Input: {x5}, Output: {result5}, Expected: {expected5} - {'Accepted' if result5 == expected5 else 'Failed'}")