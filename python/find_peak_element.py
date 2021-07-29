from typing import List


class Solution:
    def __init__(self):
        self.MIN_VALUE = -2**31

    def find(self, nums, left, right):
        if right - left == 1:
            if right == 1 and nums[left] > nums[right]:
                return 0
            elif left == len(nums) - 2 and nums[right] > nums[left]:
                return len(nums) - 1
            else:
                return -1
        else:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            ret = self.find(nums, left, mid)
            if ret > -1:
                return ret
            return self.find(nums, mid, right)

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.find(nums, 0, len(nums) - 1)


s = Solution()
print(s.findPeakElement([1, ]))
print(s.findPeakElement([1, 2,]))
print(s.findPeakElement([1, 2, 3, 4]))
print(s.findPeakElement([4, 3, 2, 1]))
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
