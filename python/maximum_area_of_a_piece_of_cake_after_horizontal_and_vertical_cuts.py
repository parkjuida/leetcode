from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        horizontalCuts.sort()

        verticalCuts.extend([0, w])
        verticalCuts.sort()

        horizontal_length = -1
        for index in range(len(horizontalCuts) - 1):
            horizontal_length = max(horizontal_length, horizontalCuts[index + 1] - horizontalCuts[index])

        vertical_length = -1
        for index in range(len(verticalCuts) - 1):
            vertical_length = max(vertical_length, verticalCuts[index + 1] - verticalCuts[index])

        return (horizontal_length * vertical_length) % (10 ** 9 + 7)


s = Solution()
print(s.maxArea(5, 4, [4, 2, 1], [3, 1]))
print(s.maxArea(5, 4, [3], [3]))
print(s.maxArea(10 ** 9, 10 ** 9, list(range(10 ** 5)), list(range(10**5))))
print(s.maxArea(10 ** 9, 10 ** 9, [2], [2]))
