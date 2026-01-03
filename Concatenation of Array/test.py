from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [1,2,1]
    result1 = sol.getConcatenation(nums1)
    expected1 = [1,2,1,1,2,1]
    print(f"Test 1: Input: {nums1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    nums2 = [1,3,2,1]
    result2 = sol.getConcatenation(nums2)
    expected2 = [1,3,2,1,1,3,2,1]
    print(f"Test 2: Input: {nums2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")