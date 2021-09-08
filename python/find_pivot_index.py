from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        left, right = 0, len(nums) - 2
        sum_ = nums[left]
        total_sum = sum(nums) - nums[left]

        while left < len(nums) - 1 and sum_ - nums[left] != total_sum:
            left += 1
            sum_ += nums[left]
            total_sum -= nums[left]

        if sum_ - nums[left] == total_sum:
            return left

        return -1


s = Solution()
print(s.pivotIndex([1, 2, 3]))
print(s.pivotIndex([3,2,1,2,3]))
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([2,1,-1]))
print(s.pivotIndex([-1,-1,0,1,1, 0,]))