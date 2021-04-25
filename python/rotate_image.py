from typing import List


class Solution:
    def swap(self, n, i, j, matrix):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - j][i]
        matrix[n - j][i] = matrix[n - i][n - j]
        matrix[n - i][n - j] = matrix[j][n - i]
        matrix[j][n - i] = temp

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for dimension in range(length // 2):
            for i in range(dimension, length - dimension - 1):
                self.swap(length - 1, dimension, i, matrix)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(matrix)
print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s = Solution()
s.rotate(matrix)
print(matrix)