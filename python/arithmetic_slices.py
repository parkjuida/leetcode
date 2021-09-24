from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        diff = [nums[i] - nums[i + 1] for i in range(len(nums) - 1)]
        answer = 0
        count = 1
        prev_d = diff[0]
        for d in diff[1:]:
            if d == prev_d:
                count += 1
            else:
                answer += max((count - 1) * count // 2, 0)
                count = 1
            prev_d = d

        answer += max((count - 1) * count // 2, 0)
        return answer


s = Solution()
print(s.numberOfArithmeticSlices([-1,-2,-3,-4]))
print(s.numberOfArithmeticSlices([0,3,5,7,9]))
print(s.numberOfArithmeticSlices([1,4,-1,-6,-11]))
print(s.numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(s.numberOfArithmeticSlices([1,2,3,6,8,10,12]))
