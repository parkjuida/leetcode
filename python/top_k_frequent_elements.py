from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        history = defaultdict(int)

        for num in nums:
            history[num] += 1

        return [x[0] for x in sorted(history.items(), key=lambda x: x[1], reverse=True)][:k]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))