from typing import List


class Solution:
    def find(self, board, row, col, word, index):
        if index == self.answer:
            return True
        ret = False
        if row - 1 >= 0 and board[row - 1][col] == word[index]:
            temp = board[row - 1][col]
            board[row - 1][col] = "-"
            ret = self.find(board, row - 1, col, word, index + 1)
            board[row - 1][col] = temp

        if ret is True:
            return ret

        if col - 1 >= 0 and board[row][col - 1] == word[index]:
            temp = board[row][col - 1]
            board[row][col - 1] = "-"
            ret = self.find(board, row, col - 1, word, index + 1)
            board[row][col - 1] = temp

        if ret is True:
            return ret
        if row + 1 < self.rows and board[row + 1][col] == word[index]:
            temp = board[row + 1][col]
            board[row + 1][col] = "-"
            ret = self.find(board, row + 1, col, word, index + 1)
            board[row + 1][col] = temp

        if ret is True:
            return ret
        if col + 1 < self.cols and board[row][col + 1] == word[index]:
            temp = board[row][col + 1]
            board[row][col + 1] = "-"
            ret = self.find(board, row, col + 1, word, index + 1)
            board[row][col + 1] = temp
        if ret is True:
            return ret

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.answer = len(word)

        ret = False
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == word[0]:
                    temp = board[row][col]
                    board[row][col] = "-"
                    ret = self.find(board, row, col, word, 1)
                    board[row][col] = temp
                if ret is True:
                    return ret

        return False


s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board, word))
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(s.exist(board, word))
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board, word))
board = [["A", "A", "A", "A"], ["A", "A", "A", "A"], ["A", "A", "A", "A"]]
word = "AAAAAAAAAAAA"
print(s.exist(board, word))
board = [["A"]]
word = "A"
print(s.exist(board, word))
board = [["A", "A"]]
word = "AAA"
print(s.exist(board, word))