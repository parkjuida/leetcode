from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for index, c in enumerate(cost):
            if index == 0 or index == 1:
                continue
            cost[index] = cost[index] + min(cost[index - 1], cost[index - 2])

        return min(cost[-1], cost[-2])

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
