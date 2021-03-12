from typing import List


class Solution:
    curr_min = 10000

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        for index, value in enumerate(nums):
            left = index + 1
            right = len(nums) - 1

            while left < right:
                s = value + nums[left] + nums[right]

                if abs(s - target) < abs(self.curr_min - target):
                    self.curr_min = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return self.curr_min

        return self.curr_min



s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([-1, 2, 1, -4], -4))
print(s.threeSumClosest([-1, 2, 1, -4], 0))
print(s.threeSumClosest([0, 0, 0], 1))
