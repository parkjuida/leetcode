from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) <= 2:
            return max(nums[-1], nums[-2])

        nums[2] = max(nums[0] + nums[2], nums[1])
        for index in range(3, len(nums)):
            nums[index] = max(nums[index - 1], nums[index] + nums[index - 2], nums[index] + nums[index - 3])

        return max(nums[-1], nums[-2])


s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
print(s.rob([1,2]))
print(s.rob([1,]))
print(s.rob([2,1,1,2]))
print(s.rob([1,7,9,2]))