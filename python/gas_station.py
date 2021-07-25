from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_index, min_cum_sum, cum_sum = 0, 0, 0

        for i in range(len(gas)):
            gas[i] -= cost[i]
            cum_sum += gas[i]

            if cum_sum < min_cum_sum:
                min_cum_sum = cum_sum
                min_index = i
                if cum_sum < 0:
                    min_index += 1

        if cum_sum < 0:
            return -1

        return min_index


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(s.canCompleteCircuit([1, 3, 1], [2, 1, 2]))
print(s.canCompleteCircuit([1, 1, 3], [2, 2, 1]))
print(s.canCompleteCircuit([3, 1, 1], [1, 2, 2]))
print(s.canCompleteCircuit([3, 1, 5], [1, 4, 2]))
print(s.canCompleteCircuit([1,], [2,]))