from typing import List


class Solution:
    def create_empty_array(self, matrix):
        new_matrix = []
        for row in range(len(matrix)):
            temp_matrix = []
            for col in range(len(matrix[0])):
                temp_matrix.append(0)

            new_matrix.append(temp_matrix)

        return new_matrix

    def create_sum_rows(self, matrix):
        sum_rows = self.create_empty_array(matrix)
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for row in range(num_rows):
            sum_rows[row][num_cols - 1] = int(matrix[row][num_cols - 1])

        for row in range(num_rows):
            for col in range(num_cols - 2, -1, -1):
                sum_rows[row][col] = 0 if matrix[row][col] == '0' else 1 + sum_rows[row][col + 1]

        return sum_rows

    def create_sum_cols(self, matrix):
        sum_cols = self.create_empty_array(matrix)
        num_rows, num_cols = len(matrix), len(matrix[0])

        for col in range(num_cols):
            sum_cols[num_rows - 1][col] = int(matrix[num_rows - 1][col])

        for col in range(num_cols):
            for row in range(num_rows - 2, -1, -1):
                sum_cols[row][col] = 0 if matrix[row][col] == '0' else 1 + sum_cols[row + 1][col]

        return sum_cols

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
            if len(matrix) == 0:
                return 0
            sum_rows = self.create_sum_rows(matrix)
            sum_cols = self.create_sum_cols(matrix)

            answer = 0
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    sr = sum_rows[row][col]
                    if sr == 0:
                        continue
                    for c in range(col + 1, col + sr + 1):
                        value = min(sum_cols[row][col:c]) * (c - col)
                        answer = max(value, answer)

            return answer


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s = Solution()
print(s.maximalRectangle(matrix))
print(s.maximalRectangle([["0", "0"]]))
matrix = [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
print(s.maximalRectangle(matrix))