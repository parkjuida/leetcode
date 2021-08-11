from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_index = 0
        for num in nums:
            if num != 0:
                nums[current_index] = num
                current_index += 1

        for index in range(current_index, len(nums)):
            nums[index] = 0


s = Solution()
a = [0, 1, 0, 3, 12]
s.moveZeroes(a)
print(a)
b = [0]
s.moveZeroes(b)
print(b)
b = [1, 0, 2, 0, 3, 0]
s.moveZeroes(b)
print(b)
b = [1]
s.moveZeroes(b)
print(b)

b = [1, 1, 1, 0, 2, 0, 3, 0]
s.moveZeroes(b)
print(b)
