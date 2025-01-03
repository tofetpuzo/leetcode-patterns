# 36. Valid Sudoku
# Medium
# Topics
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:


# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


# Constraints:


# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in col[j]
                    or board[i][j] in row[i]
                    or board[i][j] in box[(i // 3) * 3 + j // 3]
                ):
                    return False
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                box[(i // 3) * 3 + j // 3].add(board[i][j])
        return True


# other solution


def isValidSudoku(board):
    seen = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                b = (i // 3, j // 3, board[i][j])
                r = (i, board[i][j])
                c = (j, board[i][j])
                if b in seen or r in seen or c in seen:
                    return False
                seen.add(b)
                seen.add(r)
                seen.add(c)
    return True


def is_valid_sudoku(board):
    # validate rows
    for i in range(9):
        row = set()
        for j in range(9):
            item = board[i][j]
            if item in row:
                return False

            elif item != ".":
                row.add(item)

    # validate columns
    for i in range(9):
        col = set()
        for j in range(9):
            item = board[j][i]
            if item in col:
                return False
            elif item != ".":
                col.add(item)

    # validate boxes
    starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for i, j in starts:
        box_set = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                item = board[row][col]
                if item in box_set:
                    return False
                elif item != ".":
                    box_set.add(item)
    return True
