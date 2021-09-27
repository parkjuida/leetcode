from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        answer = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        if num_rows == 1:
            return min(matrix[0])

        answer[0] = matrix[0]

        for row in range(1, num_rows):
            for col in range(num_cols):
                left = answer[row - 1][max(0, col - 1)]
                mid = answer[row - 1][col]
                right = answer[row - 1][min(num_cols - 1, col + 1)]

                answer[row][col] = min(left, mid, right) + matrix[row][col]

        return min(answer[-1])


s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(s.minFallingPathSum([[-19,57],[-40,-5]]))
print(s.minFallingPathSum([[-48]]))
print(s.minFallingPathSum([[-1, -2]]))