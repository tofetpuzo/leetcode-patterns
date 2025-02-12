# 1584. Min Cost to Connect All Points
# Medium
# Topics
# Companies
# Hint
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: | xi - xj | + | yi - yj | , where | val | denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


# Example 1:


# Input: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# Output: 20
# Explanation:

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3, 12], [-2, 5], [-4, 1]]
# Output: 18


# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs(xi, yi) are distinct.
# Seen this question in a real interview before?
# 1/5
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_cost = 0

        # start Prim's algorithm from the first point
        # (cost, city_index) - cost is 0 since we start from the first point
        heap = [(0, 0)]
        num_visited = 0

        while heap and num_visited < n:
            cost, city_index = heapq.heappop(heap)

            if visited[city_index]:
                continue  # already visited

            visited[city_index] = True
            num_visited += 1
            min_cost += cost

            # explore potential tunnels to unvisited cities
            for neighbor_index in range(n):
                if not visited[neighbor_index]:
                    x1, y1 = points[city_index]
                    x2, y2 = points[neighbor_index]

                    manhattan_distance = abs(x1 - x2) + abs(y1 - y2)

                    # cost to build tunnel to neighbor
                    heapq.heappush(heap, (manhattan_distance, neighbor_index))

            # prim's needs to visit the entire nodes to complete the MST

            all_visited = all(visited)

            if all_visited:
                break

        if not all_visited:
            return float('inf')

        return min_cost


# Time complexity: O(n^2)

# Space complexity: O(n)

points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
points2 = [[3, 12], [-2, 5], [-4, 1]]

print(Solution().minCostConnectPoints(points1))  # 20
