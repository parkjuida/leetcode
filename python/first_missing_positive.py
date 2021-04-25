from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minimum = min(nums)
        positive_numbers = list(range(1, len([num for num in nums if num > 0]) + 2))

        if minimum > 1:
            return 1

        for num in nums:
            if num > 0:
                try:
                    positive_numbers[num - 1] = -1
                except IndexError:
                    pass

        for num in positive_numbers:
            if num > 0:
                return num


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7,8,9, 11, 12]))
print(s.firstMissingPositive([1, 2, 3, 4]))
print(s.firstMissingPositive([2, 3, 4]))
print(s.firstMissingPositive([1, 2, 3, 4, 6, 7, 8]))
print(s.firstMissingPositive([-1, 4, 3, 1, 6, 7, 8, 5,]))
