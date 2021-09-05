from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        prev_k = 1
        answer_map = {}
        answer = 1000000000
        while True:
            temp = sum(math.ceil(pile / k) for pile in piles)
            if k in answer_map:
                break
            answer_map[k] = temp
            if temp <= h:
                answer = min(answer, k)

            if temp > h:
                prev_k = k
                k = k * 2
            else:
                break

        low, high = prev_k, k
        while True:
            mid = (low + high) // 2
            temp = sum(math.ceil(pile / mid) for pile in piles)
            if mid in answer_map:
                break
            answer_map[mid] = temp
            if temp <= h:
                answer = min(answer, mid)

            if temp > h:
                low = mid
            else:
                high = mid

        return answer


s = Solution()
print(s.minEatingSpeed([3, 6, 7, 11], 10))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
print(s.minEatingSpeed([1000000000], 2))