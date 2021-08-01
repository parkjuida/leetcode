from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % (len(nums))

        temp = []
        for i in range(-k, 0):
            temp.append(nums[i])

        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]

        for i in range(k - 1, -1, -1):
            nums[i] = temp[i]

        return nums


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(s.rotate([-1, -100, 3, 99], 2))
print(s.rotate([1], 0))
print(s.rotate([1, 2], 0))