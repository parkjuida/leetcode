from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1

        answer = [(word_map[w], w) for w in word_map]

        answer = heapq.nsmallest(k, answer, key=lambda x: (-x[0], x[1]))

        return [e[1] for e in answer]



s = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 2
print(s.topKFrequent(words, k))
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(s.topKFrequent(words, k))
