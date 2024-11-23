# 54. Spiral Matrix
# Medium
# Topics
# Companies
# Hint
# Given an m x n matrix, return all elements of the matrix in spiral order.


# Example 1:


# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# Example 2:


# Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

def spiralOrder(matrix):
    """
        :type matrix: List[List[int]]
        :rtype: List[int]
    """
    res = []
    min_col = min_row = 0
    max_col = len(matrix[0])
    max_row = len(matrix)
    row = 0
    while min_col < max_col and min_row < max_row:

        # right
        for col in range(min_col, max_col):
            res.append(matrix[row][col])
        min_row += 1

        # down
        for row in range(min_row, max_row):
            res.append(matrix[row][col])

        max_col -= 1

        if min_col < max_col and min_row and max_row:
            # left
            for col in range(max_col- 1, min_col-1, -1):
                res.append(matrix[row][col])
            max_row -= 1

        # up
            for row in range(max_row -1 , min_row-1, -1):
                res.append(matrix[row][col])
            min_col += 1

    return res


# test cases to validate the solution

# test case 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
