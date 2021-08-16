from typing import List
from collections import deque


class Solution:
    def find_island(self, grid, row, col, num_rows, num_cols, queue):
        if grid[row][col] == 0:
            return False

        grid[row][col] = -1
        queue.append((row, col, 0))

        if row + 1 < num_rows and grid[row + 1][col] == 1:
            self.find_island(grid, row + 1, col, num_rows, num_cols, queue)
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            self.find_island(grid, row - 1, col, num_rows, num_cols, queue)
        if col + 1 < num_cols and grid[row][col + 1] == 1:
            self.find_island(grid, row, col + 1, num_rows, num_cols, queue)
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            self.find_island(grid, row, col - 1, num_rows, num_cols, queue)

        return True

    def find_path(self, queue, grid, num_rows, num_cols):
        history = set()
        while queue:
            row, col, level = queue.popleft()

            if grid[row][col] == 1:
                return level

            if row + 1 < num_rows and grid[row + 1][col] >= 0 and (row + 1, col) not in history:
                history.add((row + 1, col))
                queue.append((row + 1, col, level + 1))

            if row - 1 >= 0 and grid[row - 1][col] >= 0 and (row - 1, col) not in history:
                history.add((row - 1, col))
                queue.append((row - 1, col, level + 1))

            if col + 1 < num_cols and grid[row][col + 1] >= 0 and (row, col + 1) not in history:
                history.add((row, col + 1))
                queue.append((row, col + 1, level + 1))

            if col - 1 >= 0 and grid[row][col - 1] >= 0 and (row, col - 1) not in history:
                history.add((row, col - 1))
                queue.append((row, col - 1, level + 1))

        return -1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        queue = deque()

        for row in range(num_rows):
            ret = False
            for col in range(num_cols):
                ret = self.find_island(grid, row, col, num_rows, num_cols, queue)
                if ret:
                    break
            if ret:
                break

        return self.find_path(queue, grid, num_rows, num_cols) - 1


s = Solution()
print(s.shortestBridge([[0, 1,], [1, 0]]))
print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))