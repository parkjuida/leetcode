from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        answer = [[box[len(box) - j - 1][i] for j in range(len(box))] for i in range(len(box[0]))]

        for i in range(len(answer[0])):
            t = j = len(answer) - 1
            while t > -1:
                while t - 1 > -1 and answer[t][i] == '.':
                    t -= 1
                if t > -1 and answer[t][i] == '#':
                    answer[t][i], answer[j][i] = answer[j][i], answer[t][i]
                    j -= 1
                if t > -1 and answer[t][i] == '*':
                    j = t - 1

                t -= 1

        return answer


s = Solution()
box = [["#",".","#"]]
print(s.rotateTheBox(box))
box = [["#",".","*","."],
      ["#","#","*","."]]
print(s.rotateTheBox(box))
box = [["#","#","*",".","*","."],
      ["#","#","#","*",".","."],
      ["#","#","#",".","#","."]]
print(s.rotateTheBox(box))
