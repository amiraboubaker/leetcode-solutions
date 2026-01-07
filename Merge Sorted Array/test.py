from solution import Solution

def test_merge():
    sol = Solution()
    
    # Test case 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6], f"Expected [1,2,2,3,5,6], got {nums1}"
    
    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Expected [1], got {nums1}"
    
    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Expected [1], got {nums1}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_merge()