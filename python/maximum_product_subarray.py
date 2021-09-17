from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minus_values = [1 for _ in nums]
        answer = [0 for _ in nums]

        minus_values[0] = nums[0] if nums[0] < 0 else 0
        answer[0] = nums[0]
        maximum = answer[0]
        for i in range(1, len(nums)):
            answer[i] = max(answer[i - 1] * nums[i], minus_values[i - 1] * nums[i], nums[i])
            maximum = max(maximum, answer[i])
            minus_values[i] = min(answer[i - 1] * nums[i], minus_values[i - 1] * nums[i], nums[i])

        return maximum



s = Solution()
print(s.maxProduct([1,2,-1,-2,2,1,-2,1,4,-5,4]))
print(s.maxProduct([2,3,-2,4]))

print(s.maxProduct([2,3,-2,-1, 0, 1, 2, 100]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([2, -5, -2, -4, 3]))
print(s.maxProduct([7, -2, -4]))
print(s.maxProduct([-2]))
print(s.maxProduct([2,-1,1,1]))