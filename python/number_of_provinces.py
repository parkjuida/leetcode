from typing import List


class Solution:
    def find_province(self, map_, provinces, row, answer, n_row, n_col):
        if provinces[row] > 0:
            return
        provinces[row] = answer
        for col in range(n_col):
            if row == col:
                continue
            if map_[row][col] == 1 and provinces[col] == 0:
                self.find_province(map_, provinces, col, answer, n_row, n_col)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_row, n_col = len(isConnected), len(isConnected[0])
        provinces = [0 for _ in range(n_row)]
        answer = 0
        for row in range(n_row):
            for col in range(n_col):
                if row == col and provinces[row] == 0:
                    answer += 1
                    provinces[row] = answer
                if isConnected[row][col] == 1:
                    self.find_province(isConnected, provinces, col, answer, n_row, n_col)

        return answer


s = Solution()
# print(s.findCircleNum([
#     [1, 1, 0],
#     [1, 1, 0],
#     [0, 0, 1]]))
# print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
print(s.findCircleNum([
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]]
)
)

print(s.findCircleNum([
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
]))