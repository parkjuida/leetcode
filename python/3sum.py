from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = set()
        l = len(nums)
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = l - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        answer = [list(a) for a in answer]
        return answer


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([]))
print(s.threeSum([0]))
print(s.threeSum([0, 0, 0]))
