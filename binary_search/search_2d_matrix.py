# 74. Search a 2D Matrix
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
def searchMatrix(matrix, target):
    """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
    """
    row = len(matrix)
    col = len(matrix[0])
    t = row * col
    l, r = 0, t - 1
    while l <= r:
        mid = (l + r) // 2
        row_index = mid // col
        col_index = mid % col
        mid_val = matrix[row_index][col_index]
        if mid_val == target:
            return True
        elif target < mid_val:
            r = mid - 1
        else:
            l = mid + 1
    return False

# Time complexity: O(log(m * n))
# Space complexity: O(1)


# test case
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))  # True
