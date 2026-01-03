from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [2,5,1,3,4,7]
    n1 = 3
    result1 = sol.shuffle(nums1, n1)
    expected1 = [2,3,5,4,1,7]
    print(f"Test 1: Input: {nums1}, n={n1}, Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    nums2 = [1,2,3,4,4,3,2,1]
    n2 = 4
    result2 = sol.shuffle(nums2, n2)
    expected2 = [1,4,2,3,3,2,4,1]
    print(f"Test 2: Input: {nums2}, n={n2}, Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
    
    # Test Case 3
    nums3 = [1,1,2,2]
    n3 = 2
    result3 = sol.shuffle(nums3, n3)
    expected3 = [1,2,1,2]
    print(f"Test 3: Input: {nums3}, n={n3}, Output: {result3}, Expected: {expected3} - {'Accepted' if result3 == expected3 else 'Failed'}")