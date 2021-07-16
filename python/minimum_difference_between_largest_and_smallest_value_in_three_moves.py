from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)

        answer = 10**10

        n = len(nums)
        if n < 5:
            return 0

        for i in range(4):
            answer = min(nums[n + -4 + i] - nums[i], answer)

        return answer


s = Solution()
print(s.minDifference([5, 3, 2, 4]))
print(s.minDifference([1, 5, 0, 10, 14]))
print(s.minDifference([6, 6, 0, 1, 1, 4, 6]))
print(s.minDifference([1, 5, 6, 14, 15]))
