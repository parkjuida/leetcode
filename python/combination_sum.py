from typing import List


class Solution:
    def combination(self, candidates, candidate_index, target, current, answer):
        if target == 0:
            answer.append(current)
            return
        if target < 0:
            return
        for i in range(candidate_index, len(candidates)):
            self.combination(candidates, i, target - candidates[i], current + [candidates[i]], answer)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.combination(candidates, 0, target, [], answer)
        return answer

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
print(s.combinationSum([1], 1))
print(s.combinationSum([1], 2))