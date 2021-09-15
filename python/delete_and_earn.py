from typing import List
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sub_sum = defaultdict(int)
        start_value = 10000
        end_value = 1
        for num in nums:
            sub_sum[num] += num
            if start_value > num:
                start_value = num
            if end_value < num:
                end_value = num

        for i in range(start_value, end_value + 1):
            sub_sum[i] = max(sub_sum[i] + sub_sum[i - 2], sub_sum[i - 1])

        return sub_sum[end_value]


s = Solution()
print(s.deleteAndEarn([3,4,2]))
print(s.deleteAndEarn([2,2,3,3,3,4]))
print(s.deleteAndEarn([1]))
print(s.deleteAndEarn([1, 1, 1, 2, 3]))