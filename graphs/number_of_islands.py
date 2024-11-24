# 200. Number of Islands
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's(land) and '0's(water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# Output: 3


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
        """

    cols = len(grid[0])
    rows = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1),  (0, -1)]
    num_islands = 0

    def dfs(grid, r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
            grid[r][c] = "0"
            for row_inc, col_inc in directions:
                dfs(grid, r+row_inc, c+col_inc)


    for col in range(cols):
        for row in range(rows):
            if grid[row][col] == "1":
                num_islands +=1
                dfs(grid, row, col)

    return num_islands

# Time: O(m*n)
# Space: O(1)

# Test case
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))  # 3
