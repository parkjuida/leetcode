from typing import List


class Solution:
    def calculate(self, matrix, row, col, size):
        while size > 0:
            trap = False
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if matrix[i][j] == 0:
                        trap = True
                        size -= 1
                        break
                if trap:
                    break
            if not trap:
                return size
        return 0

    def countSquares(self, matrix: List[List[int]]) -> int:
        row_nums = len(matrix)
        col_nums = len(matrix[0])

        row_sides = [[0 for _ in range(col_nums)] for _ in range(row_nums)]
        col_sides = [[0 for _ in range(col_nums)] for _ in range(row_nums)]

        for row in range(row_nums - 1, -1, -1):
            for col in range(col_nums - 1, -1, -1):
                if row == row_nums - 1:
                    row_sides[row][col] = matrix[row][col]
                elif matrix[row][col] != 0:
                    row_sides[row][col] = row_sides[row + 1][col] + matrix[row][col]

        for col in range(col_nums - 1, -1, -1):
            for row in range(row_nums - 1, -1, -1):
                if col == col_nums - 1:
                    col_sides[row][col] = matrix[row][col]
                elif matrix[row][col] != 0:
                    col_sides[row][col] = col_sides[row][col + 1] + matrix[row][col]

        answer = 0

        for row in range(row_nums):
            for col in range(col_nums):
                size = min(row_sides[row][col], col_sides[row][col])
                ret = self.calculate(matrix, row, col, size)
                answer += ret

        return answer


s = Solution()
print(s.countSquares(
    [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]
))
print(s.countSquares(
    [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
))
print(s.countSquares(
    [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
))
print(s.countSquares(
    [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]
))
print([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ])
