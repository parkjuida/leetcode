from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        contain_zero_rows = False
        contain_zero_cols = False
        for i in range(0, num_rows):
            if matrix[i][0] == 0:
                contain_zero_rows = True
        for j in range(0, num_cols):
            if matrix[0][j] == 0:
                contain_zero_cols = True

        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, num_rows):
            if matrix[i][0] == 0:
                for j in range(num_cols):
                    matrix[i][j] = 0

        for j in range(1, num_cols):
            if matrix[0][j] == 0:
                for i in range(num_rows):
                    matrix[i][j] = 0

        if contain_zero_rows is True:
            for i in range(0, num_rows):
                matrix[i][0] = 0
        if contain_zero_cols is True:
            for j in range(0, num_cols):
                matrix[0][j] = 0
