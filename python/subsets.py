from typing import List


class Solution:
    def create(self, index, nums):
        if index == len(nums) - 1:
            return [[], [nums[index]]]
        ret = self.create(index + 1, nums)
        answer = []
        for r in ret:
            answer.append(r)
            answer.append([*r, nums[index]])
        return answer

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.create(0, nums)

s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([0]))