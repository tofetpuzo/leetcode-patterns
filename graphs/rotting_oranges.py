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

from collections import deque


def orangesRotting(grid):
    """
        :type grid: List[List[int]]
        :rtype: int
        """
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
    
    num_of_fresh = 0
    q = deque()

    rows = len(grid)
    cols = len(grid[0])

    # populate the grid to know the fresh, rotten and empty oranges
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == FRESH:
                num_of_fresh += 1
            elif grid[i][j] == ROTTEN:
                q.append((i, j))
    
    # check for the 4 directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes = 0
    
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != FRESH:
                    continue
                grid[x][y] = ROTTEN
                num_of_fresh -= 1
                q.append((x, y))
        minutes += 1
    # if there are no fresh oranges, return the minutes
    if num_of_fresh == EMPTY:
        return minutes - 1
    
    # if there are fresh oranges, return -1
    return -1
        
# Complexity Analysis
# The time complexity for this approach is O(m*n) where m is the number of rows and n is the number of columns in the grid.s
    


# Time: O(m*n)
# Space: O(m*n) 

# Test case
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]


print(orangesRotting(grid))  # 4

