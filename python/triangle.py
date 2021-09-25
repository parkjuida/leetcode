from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answer = [[10000000 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        answer[0][0] = triangle[0][0]

        for i in range(0, len(triangle) - 1):
            for j in range(len(triangle[i])):
                answer[i + 1][j] = min(answer[i][j] + triangle[i + 1][j], answer[i + 1][j])
                answer[i + 1][j + 1] = min(answer[i][j] + triangle[i + 1][j + 1], answer[i + 1][j + 1])

        return min(answer[-1])


s = Solution()
print(s.minimumTotal( [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal( [[-10]]))
