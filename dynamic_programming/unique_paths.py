# 62. Unique Paths
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner(i.e., grid[0][0]). The robot tries to move to the bottom-right corner(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


# Constraints:

# 1 <= m, n <= 100
class Solution(object):
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # top down dp(memoization)
        memo = {(0, 0): 1}

        def paths(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                memo[(i, j)] = paths(i - 1, j) + paths(i, j - 1)
                return memo[(i, j)]

        return paths(m - 1, n - 1)

    # bottom up approach
    def unique_paths_bottom_up(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                val  = 0
                if i > 0:
                    val += dp[i - 1][j]
                if j > 0:
                    val += dp[i][j - 1]

                dp[i][j] = val

        return dp[m - 1][n - 1]

    # bottom up approach with space optimization
# Time complexity: O(m*n)
# Space complexity: O(m*n)


# test cases to validate the solution
# test case 1
sol = Solution
print(sol.unique_paths(sol, 3, 7))  #
# test case 2
print(sol.unique_paths(sol, 3, 2))  #
# test case 3
print(sol.unique_paths(sol, 3, 3))  #
# test case 4
print(sol.unique_paths(sol, 3, 4))  #
# test case 5
print(sol.unique_paths(sol, 3, 5))  #
# test case 6
print(sol.unique_paths(sol, 3, 6))  #
# test case 7
print(sol.unique_paths(sol, 3, 8))  #


# optimized solution
# Time complexity: O(m*n)
# Space complexity: O(n)
# test cases to validate the solution
