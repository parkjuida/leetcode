from typing import List


class Solution:
    def isValidBlock(self, number, cache, index):
        try:
            if number in cache[index]:
                return False
            cache[index].append(number)
        except KeyError:
            cache[index] = [number]

        return True

    def get_zone(self, i, j):
        return i // 3, j // 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_cache = {}
        row_cache = {}
        zone_cache = {}

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == ".":
                    continue
                z = self.get_zone(i, j)
                if not self.isValidBlock(number, row_cache, i):
                    return False
                if not self.isValidBlock(number, col_cache, j):
                    return False
                if not self.isValidBlock(number, zone_cache, z):
                    return False

        return True


s = Solution()
print(s.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
)

print(s.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
)