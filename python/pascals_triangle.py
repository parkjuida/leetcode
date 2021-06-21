
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        answer = [[1], [1, 1]]

        depth = 2
        while depth < numRows:
            temp = [1]
            temp.extend([answer[-1][i] + answer[-1][i + 1] for i in range(depth - 1)])
            temp.append(1)

            answer.append(temp)
            depth += 1

        return answer


s = Solution()
print(s.generate(1))
print(s.generate(5))
