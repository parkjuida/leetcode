from typing import List


class Solution:
    def get_next_iterator(self, index, height, length):
        max_index = index + 1
        for j in range(index + 1, length):
            if height[j] >= height[index]:
                return j
            if height[j] > height[max_index]:
                max_index = j

        return max_index

    def calculate(self, start, end, height):
        min_poll = min(height[start], height[end])
        rain = 0
        for i in range(start + 1, end):
            rain += (min_poll - height[i])

        return rain

    def trap(self, height: List[int]) -> int:
        length = len(height)
        iterator = 0
        rain = 0
        while iterator < length:
            next_iterator = self.get_next_iterator(iterator, height, length)
            if next_iterator == length:
                break
            rain += self.calculate(iterator, next_iterator, height)
            iterator = next_iterator

        return rain


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
print(s.trap([4, 1, 2]))
print(s.trap([4, 1, 5]))
print(s.trap([4, 1, 4, 1, 4]))
print(s.trap([9999, 0, 9999] * 10 ** 4))