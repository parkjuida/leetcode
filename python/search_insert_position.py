from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right - 1:
            center = (left + right) // 2

            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center
            else:
                right = center

        if target <= nums[left]:
            return left
        elif nums[left] < target and target <= nums[right]:
            return right
        else:
            return right + 1


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
print(s.searchInsert([1], 0))
print(s.searchInsert([1], 1))
print(s.searchInsert([1], 2))