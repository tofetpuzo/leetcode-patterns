# 939. Minimum Area Rectangle
# Medium
# Topics
# Companies
# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.


# Example 1:


# Input: points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
# Output: 4
# Example 2:


# Input: points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
# Output: 2


# Constraints:

# 1 <= points.length <= 500
# points[i].length == 2
# 0 <= xi, yi <= 4 * 104
# All the given points are unique.
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # O(n^2)
        # brute force
        # for each pair of points, check if the other two points exist
        # if they do, calculate the area
        # keep track of the minimum area
        # return the minimum area
        # O(n^2)
        # O(n)
        # O(n)
        # O(1)

        points_set = set(map(tuple, points))
        min_area = float('inf')
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        min_area = min(min_area, abs(x1-x2) * abs(y1-y2))
        return min_area if min_area != float('inf') else 0


points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
# # Output: 4

print(Solution().minAreaRect(points))  # 4
