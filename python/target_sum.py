from typing import List


class Solution:
    def find(self, start, n, nums, target, history):
        if start == n:
            if target == 0:
                return 1
            else:
                return 0

        if (start, target) in history:
            return history[(start, target)]
        answer = self.find(start + 1, n, nums, target - nums[start], history)
        answer += self.find(start + 1, n, nums, target + nums[start], history)

        history[(start, target)] = answer
        return answer

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        history = dict()
        return self.find(0, len(nums), nums, target, history)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays([1], 1))
print(s.findTargetSumWays([10, 2], 8))