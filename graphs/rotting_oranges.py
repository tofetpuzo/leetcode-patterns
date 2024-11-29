# 994. Rotting Oranges
# Medium
# Topics
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:


# Input: grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4
# Example 2:

# Input: grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1
# Explanation: The orange in the bottom left corner(row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0, 2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
def orangesRotting(grid):
    """
        :type grid: List[List[int]]
        :rtype: int
        """
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

    rows = len(grid)
    cols = len(grid[0])

    def dfs(grid, row, col, minutes):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != FRESH:
            return
        grid[row][col] = minutes
        dfs(grid, row + 1, col, minutes + 1)
        dfs(grid, row - 1, col, minutes + 1)
        dfs(grid, row, col + 1, minutes + 1)
        dfs(grid, row, col - 1, minutes + 1)
    
    minutes = 0
    while True:
        changed = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == ROTTEN:
                    dfs(grid, row, col, minutes + 1)
                    changed = True
        if not changed:
            break
        minutes += 1
    if any(FRESH in row for row in grid):
        return -1
    
    return minutes


# Time: O(m*n)
# Space: O(m*n) 

# Test case
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]


print(orangesRotting(grid))  # 4

