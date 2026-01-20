from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    mat1 = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
    threshold1 = 4
    result1 = sol.maxSideLength(mat1, threshold1)
    expected1 = 2  # Assuming
    print(f"Test 1: Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")
    
    # Test Case 2
    mat2 = [[2,2,2],[2,2,2],[2,2,2]]
    threshold2 = 10
    result2 = sol.maxSideLength(mat2, threshold2)
    expected2 = 2  # 2x2 sum=8 <=10, 3x3=18>10
    print(f"Test 2: Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")