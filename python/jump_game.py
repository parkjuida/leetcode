from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        on = [0 for _ in range(len(nums))]
        on[0] = 1
        max_on_index = 1
        for i in range(len(nums) - 1):
            if on[i] == 0:
                continue
            for to_go in range(max(max_on_index, i), min(i + nums[i] + 1, len(nums))):
                on[to_go] = 1

            max_on_index = i + nums[i]

        if on[-1] == 1:
            return True
        else:
            return False


s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([0,2,3]))