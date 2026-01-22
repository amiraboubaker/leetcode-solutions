from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Already non-decreasing
    nums1 = [1, 2, 3]
    result1 = sol.minimumPairRemoval(nums1)
    expected1 = 0
    print(f"Test 1: Input: {nums1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2: Decreasing array
    nums2 = [3, 2, 1]
    result2 = sol.minimumPairRemoval(nums2)
    expected2 = 1
    print(f"Test 2: Input: {nums2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3: Mixed
    nums3 = [1, 3, 2]
    result3 = sol.minimumPairRemoval(nums3)
    expected3 = 2
    print(f"Test 3: Input: {nums3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")