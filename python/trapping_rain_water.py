from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        rain = 0
        temp_rain = 0
        current_max = 0

        for i in range(length):
            if height[current_max] < height[i]:
                rain += temp_rain
                temp_rain = 0
                current_max = i

            temp_rain += (height[current_max] - height[i])

        maximum_index = current_max
        current_max = length - 1
        temp_rain = 0
        for i in range(length - 1, maximum_index - 1, -1):
            if height[current_max] <= height[i]:
                rain += temp_rain
                temp_rain = 0
                current_max = i

            temp_rain += (height[current_max] - height[i])

        return rain


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
print(s.trap([4, 1, 2]))
print(s.trap([4, 1, 5]))
print(s.trap([4, 1, 4, 1, 4]))
print(s.trap([9999, 0, 9999] * 10 ** 4))