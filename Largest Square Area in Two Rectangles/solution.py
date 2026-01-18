class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        maxArea = 0

        for i in range(n):
            for j in range(i + 1, n):
                x_left = max(bottomLeft[i][0], bottomLeft[j][0])
                y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                x_right = min(topRight[i][0], topRight[j][0])
                y_top = min(topRight[i][1], topRight[j][1])

                width = x_right - x_left
                height = y_top - y_bottom

                if width > 0 and height > 0:
                    side = min(width, height)
                    maxArea = max(maxArea, side * side)

        return maxArea