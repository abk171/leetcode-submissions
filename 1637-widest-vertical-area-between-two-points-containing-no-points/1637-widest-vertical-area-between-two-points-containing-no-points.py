class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        maxdiff = abs(points[1][0] - points[0][0])
        for i in range(2,len(points)):
            maxdiff = max(maxdiff, abs(points[i][0] - points[i - 1][0]))
        return maxdiff