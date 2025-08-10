# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_row = min_col = 0
        max_row = len(matrix)
        max_col = len(matrix[0])
        row = 0
        """
         min_col       max_col
        [[1,2,3], min_row
        [4,5,6],
        [7,8,9]] max_row"""
        res = []
        while min_row < max_row and min_col < max_col:
            # right
            for col in range(min_col, max_col):
                res.append(matrix[row][col])
            min_row +=1

            # down
            for row in range(min_row, max_row):
                res.append(matrix[row][col])

            max_col -=1

            if min_col < max_col and min_row < max_row:
                # down
                for col in range(max_col- 1, min_col-1, -1):
                    res.append(matrix[row][col])
                max_row-=1
                
                # left
                for row in range(max_row- 1, min_row-1, -1):
                    res.append(matrix[row][col])
                min_col+=1
               

        return res