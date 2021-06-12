# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# Example 1:
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
from pprint import pprint
from queue import LifoQueue

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def solveSudoku(board: list) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    board_current = [row[::] for row in board]  # текущее положение доски

    def validate_list(lst: list) -> bool:  # numbers should not repeat
        return True if len(lst) == len(set(lst)) else False

    def check_row(row: int) -> bool:  # checks row 0 - 8
        # print(board_current[row])
        return validate_list([item for item in board_current[row] if item != '.'])

    def check_column(column: int) -> bool:  # checks column 0 - 8
        # print([row[column] for row in board_current])
        return validate_list([row[column] for row in board_current if row[column] != '.'])

    def check_subarea(row: int, column: int) -> bool:  # checks row 0 - 8 and column 0 - 8 with area 3x3
        def subarea_range(i: int) -> range:
            if i < 3:
                return range(3)
            elif i >= 6:
                return range(6, 9)
            else:
                return range(3, 6)

        subarea = [board_current[row_i][column_i] for column_i in subarea_range(column) for row_i in subarea_range(row)
                   if board_current[row_i][column_i] != '.']
        return validate_list(subarea)

    def check_board(row: int, column: int) -> bool:
        if check_row(row) and check_column(column) and check_subarea(row, column):
            return True
        else:
            return False

    def get_next_cell(row: int, column: int):
        while row < len(board) and board_current[row][column] != '.':
            column += 1
            if column > len(board_current[0]) - 1:
                row += 1
                column = 0
        return row, column

    def get_prev_cell(row: int, column: int):
        cur_point = row, column
        # if column == 8:
        # print(column)
        while board[row][column] != '.' or (row, column) == cur_point:
            column -= 1
            if column < 0:
                row -= 1
                column = len(board_current[0]) - 1
        return row, column

    r = c = 0  # current row, col
    while board_current[r][c] != '.':
        c += 1
        if c > len(board_current[0]) - 1:
            r += 1
            c = 0
        if r > len(board_current[0]) - 1:
            return
    while r < len(board_current):
        if board_current[r][c] == '.':
            board_current[r][c] = '1'
        if not check_board(r, c):
            if board_current[r][c] == '9':
                while board_current[r][c] == '9':
                    board_current[r][c] = '.'
                    r, c = get_prev_cell(r, c)
            board_current[r][c] = str(int(board_current[r][c]) + 1)

        else:
            r, c = get_next_cell(r, c)
    for i in range(0, 9):
        for j in range(0, 9):
            board[i][j] = board_current[i][j]


# pprint(board)
solveSudoku(board)
pprint(board)
