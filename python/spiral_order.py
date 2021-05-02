class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        total_num = num_rows * num_cols
        min_spiral = min(num_rows // 2, num_cols // 2)
        answer = []
        index = 0

        while index <= min_spiral:
            x, y = index, index
            for i in range(x, num_cols - index - 1):
                answer.append(matrix[y][i])
            x, y = num_cols - index - 1, index
            for i in range(y, num_rows - index - 1):
                answer.append(matrix[i][x])
            x, y = num_cols - index - 1, num_rows - index - 1
            for i in range(x, index, -1):
                answer.append(matrix[y][i])
            x, y = index, num_rows - index - 1
            for i in range(y, index, -1):
                answer.append(matrix[i][x])

            index += 1

        if len(answer) + 1 == total_num:
            answer.append(matrix[index - 1][index - 1])
        return answer[:total_num]