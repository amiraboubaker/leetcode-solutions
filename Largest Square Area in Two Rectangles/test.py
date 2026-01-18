import unittest
from solution import Solution

class TestLargestSquareArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_rectangles_intersect_small(self):
        bottomLeft = [[1,1],[3,3]]
        topRight = [[4,4],[6,6]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 1)

    def test_no_intersection(self):
        bottomLeft = [[1,1],[5,5]]
        topRight = [[3,3],[7,7]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 0)

    def test_larger_intersection(self):
        bottomLeft = [[0,0],[1,1]]
        topRight = [[3,3],[4,4]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 4)

    def test_three_rectangles(self):
        bottomLeft = [[0,0],[1,1],[2,2]]
        topRight = [[3,3],[4,4],[5,5]]
        # Pairs: 0-1: as above, 4; 0-2: x_left=max(0,2)=2, y=2, x_right=min(3,5)=3, y=3, w=1,h=1,a=1; 1-2: x=max(1,2)=2,y=2,x=min(4,5)=4,y=4,w=2,h=2,a=4
        # Max 4
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 4)

if __name__ == '__main__':
    unittest.main()