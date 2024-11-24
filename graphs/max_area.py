# 695. Max Area of Island
# Solved
# Medium
# Topics
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

def max_area_of_island(grid):
	cols = len(grid[0])
	rows = len(grid)

	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	max_area_of_island = 0


	def dfs(grid, r, c):
		if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
			area = 1
			grid[r][c] = 0
			for row_inc, col_inc in directions:
				area+=dfs(grid, r+row_inc, c+col_inc)
			return area

		return 0


	for col in range(cols):
		for row in range(rows):
			if grid[row][col] == 1:
				max_area_of_island = max(max_area_of_island, dfs(grid, row, col))

	return max_area_of_island




# Time: O(m*n)
# Space: O(1)

# Test case

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(max_area_of_island(grid))  # 6