from typing import List

class Solution:
    def find(self, grid, visited, row, col):
        if grid[row][col] == 0 or visited[row][col] is True:
            return 0

        visited[row][col] = True
        answer = 1

        if row - 1 >= 0:
            answer += self.find(grid, visited, row - 1, col)
        if row + 1 < len(grid):
            answer += self.find(grid, visited, row + 1, col)
        if col - 1 >= 0:
            answer += self.find(grid, visited, row, col - 1)
        if col + 1 < len(grid[0]):
            answer += self.find(grid, visited, row, col + 1)

        return answer

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] is True:
                    continue

                answer = max(answer, self.find(grid, visited, i, j))

        return answer


s = Solution()
print(s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
print(s.maxAreaOfIsland(
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
))
