from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = [100000] * len(nums)

        answer[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != 0:
                answer[i] = min(answer[i:i + nums[i] + 1]) + 1

        return answer[0]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
print(s.jump([1, 1, 1, 3, 1]))
print(s.jump([2, 1]))