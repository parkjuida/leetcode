from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_nums = len(grid)
        col_nums = len(grid[0])

        q = deque()
        history = set()

        for row in range(row_nums):
            for col in range(col_nums):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
                    history.add((row, col))

        answer = 0
        while q:
            row, col, minutes = q.popleft()
            answer = max(minutes, answer)
            if row + 1 < row_nums and grid[row + 1][col] == 1 and (row + 1, col) not in history:
                grid[row + 1][col] = 2
                q.append((row + 1, col, minutes + 1))
            if row - 1 >= 0 and grid[row - 1][col] == 1 and (row - 1, col) not in history:
                grid[row - 1][col] = 2
                q.append((row - 1, col, minutes + 1))
            if col + 1 < col_nums and grid[row][col + 1] == 1 and (row, col + 1) not in history:
                grid[row][col + 1] = 2
                q.append((row, col + 1, minutes + 1))
            if col - 1 >= 0 and grid[row][col - 1] == 1 and (row, col - 1) not in history:
                grid[row][col - 1] = 2
                q.append((row, col - 1, minutes + 1))

        for row in range(row_nums):
            for col in range(col_nums):
                if grid[row][col] == 1:
                    answer = -1

        return answer


s = Solution()
print(s.orangesRotting([[2, 1, 1,], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0, 2]]))
print(s.orangesRotting([[0]]))
print(s.orangesRotting([[1]]))
print(s.orangesRotting([[2]]))
print(s.orangesRotting([[0, 1], [0, 1]]))