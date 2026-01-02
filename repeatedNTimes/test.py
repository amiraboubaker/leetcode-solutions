from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3, 3]
    result1 = sol.repeatedNTimes(nums1)
    expected1 = 3
    print(f"Test 1: Input: {nums1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    nums2 = [2, 1, 2, 5, 3, 2]
    result2 = sol.repeatedNTimes(nums2)
    expected2 = 2
    print(f"Test 2: Input: {nums2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3
    nums3 = [5, 1, 5, 2, 5, 3, 5, 4]
    result3 = sol.repeatedNTimes(nums3)
    expected3 = 5
    print(f"Test 3: Input: {nums3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")