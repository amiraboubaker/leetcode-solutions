from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [2, 3, 5, 7]
    result1 = sol.minBitwiseArray(nums1)
    expected1 = [-1, 1, 4, 3]
    print(f"Test 1: Input: {nums1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    nums2 = [1]
    result2 = sol.minBitwiseArray(nums2)
    expected2 = [0]
    print(f"Test 2: Input: {nums2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3
    nums3 = [9, 11, 15]
    result3 = sol.minBitwiseArray(nums3)
    expected3 = [8, 9, 7]
    print(f"Test 3: Input: {nums3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")