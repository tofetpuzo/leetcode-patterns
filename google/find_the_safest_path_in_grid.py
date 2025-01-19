# 812. Find the Safest Path in a Grid
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed 2D matrix grid of size n x n, where(r, c) represents:

# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# You are initially positioned at cell(0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

# The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

# Return the maximum safeness factor of all paths leading to cell(n - 1, n - 1).

# An adjacent cell of cell(r, c), is one of the cells(r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

# The Manhattan distance between two cells (a, b) and (x, y) is equal to | a - x | + | b - y | , where | val | denotes the absolute value of val.


# Example 1:


# Input: grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
# Output: 0
# Explanation: All paths from (0, 0) to(n - 1, n - 1) go through the thieves in cells(0, 0) and (n - 1, n - 1).
# Example 2:


# Input: grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell(0, 2) is cell(0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.
# Example 3:


# Input: grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell(0, 3) is cell(1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
# - The closest cell of the path to the thief at cell(3, 0) is cell(3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.


# Constraints:

# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        from collections import deque
        import heapq

        def in_bound(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        def precompute():
            min_dist = {}
            q = deque()
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            while q:
                r, c, dist = q.popleft()
                nei = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
                for nr, rc in nei:
                    if in_bound(nr, rc) and (nr, rc) not in min_dist:
                        min_dist[(nr, rc)] = dist + 1
                        q.append([nr, rc, dist + 1])
            return min_dist

        min_dist = precompute()
        max_heap = [(-min_dist[(0, 0)], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = - dist
            if (r, c) == (N - 1, N - 1):
                return dist
            nei = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for nr, nc in nei:
                if in_bound(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dist2 = min(dist, min_dist[(nr, nc)])
                    heapq.heappush(max_heap, (-dist2, nr, nc))


grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
# Output: 0
print(Solution().maximumSafenessFactor(grid))

grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
# Output: 2
print(Solution().maximumSafenessFactor(grid))

grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]

# Output: 2
print(Solution().maximumSafenessFactor(grid))
