from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1_1 = [2,1,-2,5]
    nums2_1 = [3,0,-6]
    result1 = sol.maxDotProduct(nums1_1, nums2_1)
    expected1 = 18
    print(f"Test 1: Input: {nums1_1}, {nums2_1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    nums1_2 = [3,-2]
    nums2_2 = [2,-6,7]
    result2 = sol.maxDotProduct(nums1_2, nums2_2)
    expected2 = 21
    print(f"Test 2: Input: {nums1_2}, {nums2_2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3
    nums1_3 = [-1,-1]
    nums2_3 = [1,1]
    result3 = sol.maxDotProduct(nums1_3, nums2_3)
    expected3 = -1
    print(f"Test 3: Input: {nums1_3}, {nums2_3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")