# 200. Number of Islands
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

from collections import deque
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        def bfs(r: int, c: int):
            queue = deque([(r, c)])
            visited[r][c] = True
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    nr, nc = x + dx, y + dy
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == '1':
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r, c)
                    island_count += 1
        return island_count

def numIslands(self, grid: List[List[str]]) -> int:  
    cols = len(grid[0])
    rows = len(grid)
    nums_islands = 0

    def dfs(grid, r, c):
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
            grid[r][c] = "0"
            for r_inc, c_inc in dir:
                dfs(grid , r+r_inc, c+c_inc)

    for col in range(cols):
        for row in range(rows):
            if grid[row][col] == "1":
                nums_islands+=1
                dfs(grid, row, col)
    return nums_islands