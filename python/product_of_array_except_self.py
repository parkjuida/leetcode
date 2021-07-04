from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number_of_zero, total_multiplied = 0, 1
        for num in nums:
            if num == 0:
                number_of_zero += 1
            else:
                total_multiplied *= num

        for i in range(len(nums)):
            if number_of_zero > 1:
                nums[i] = 0
                continue

            if nums[i] == 0:
                nums[i] = total_multiplied
                continue

            if number_of_zero == 1:
                nums[i] = 0
            else:
                nums[i] = int(total_multiplied / nums[i])

        return nums


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
