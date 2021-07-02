from typing import List


class Solution:
    def findIsland(self, grid, visited, i, j):
        visited[i][j] = 1

        if i + 1 < len(grid) and grid[i + 1][j] == "1" and visited[i + 1][j] == 0:
            self.findIsland(grid, visited, i + 1, j)
        if i - 1 > -1 and grid[i - 1][j] == "1" and visited[i - 1][j] == 0:
            self.findIsland(grid, visited, i - 1, j)

        if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and visited[i][j + 1] == 0:
            self.findIsland(grid, visited, i, j + 1)
        if j - 1 > -1 and grid[i][j - 1] == "1" and visited[i][j - 1] == 0:
            self.findIsland(grid, visited, i, j - 1)

        return 1


    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    answer += self.findIsland(grid, visited, i, j)

        return answer

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
s = Solution()
print(s.numIslands(grid))
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))
grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
print(s.numIslands(grid))
