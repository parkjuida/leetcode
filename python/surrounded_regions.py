from typing import List


class Solution:
    def judge(self, row, col, board):
        row_len = len(board)
        col_len = len(board[0])

        if board[row][col] != 'O':
            return
        board[row][col] = 'E'

        if row + 1 < row_len:
            self.judge(row + 1, col, board)
        if row > 0:
            self.judge(row - 1, col, board)
        if col + 1 < col_len:
            self.judge(row, col + 1, board)
        if col > 0:
            self.judge(row, col - 1, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for col in range(0, len(board[0])):
            if board[0][col] == 'O':
                self.judge(0, col, board)

        for row in range(0, len(board)):
            if board[row][len(board[0]) - 1] == 'O':
                self.judge(row, len(board[0]) - 1, board)

        for col in range(0, len(board[0])):
            if board[len(board) - 1][col] == 'O':
                self.judge(len(board) - 1, col, board)

        for row in range(0, len(board)):
            if board[row][0] == 'O':
                self.judge(row, 0, board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "E":
                    board[row][col] = "O"


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s = Solution()
s.solve(board)
board = [["O"]]
s.solve(board)
print(board)
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","O"],["X","O","X","X"]]
s.solve(board)
print(board)
board = [
    ["O","O","O","O","X","X"],
    ["O","O","O","O","O","O"],
    ["O","X","O","X","O","O"],
    ["O","X","O","O","X","O"],
    ["O","X","O","X","O","O"],
    ["O","X","O","O","O","O"]
]
s.solve(board)
print(board)