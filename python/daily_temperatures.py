from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [-1]
        for index, temperature in enumerate(temperatures):
            if stack[-1] != -1:
                while stack[-1] != -1 and stack[-1][1] < temperature:
                    prev_index, value = stack.pop()
                    answer[prev_index] = index - prev_index

            stack.append((index, temperature))

        return answer


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([30, 40, 50, 60]))
print(s.dailyTemperatures([30, 60, 90]))
print(s.dailyTemperatures([30, 20, 10, 40, 50]))