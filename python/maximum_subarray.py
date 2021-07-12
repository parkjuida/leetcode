from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumulative_sum = 0
        answer = -10 ** 5

        for num in nums:
            cumulative_sum += num

            answer = max(answer, cumulative_sum)

            if cumulative_sum < 0:
                cumulative_sum = 0

        return answer


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
print(s.maxSubArray([-2, -1]))