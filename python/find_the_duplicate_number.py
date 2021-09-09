from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            to_swap_index = nums[i] - 1
            if i == to_swap_index:
                continue
            if nums[i] == nums[to_swap_index]:
                return nums[i]

            while nums[i] != i + 1:
                nums[i], nums[to_swap_index] = nums[to_swap_index], nums[i]

                if nums[i] == nums[to_swap_index]:
                    return nums[i]

                to_swap_index = nums[i] - 1


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
print(s.findDuplicate([3, 1, 3, 4, 2]))
print(s.findDuplicate([1, 1]))
print(s.findDuplicate([1, 1, 2]))
print(s.findDuplicate([2,1,2]))
print(s.findDuplicate([1, 3, 2, 4, 2]))
print(s.findDuplicate([8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18]))