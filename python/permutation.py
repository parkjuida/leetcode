from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = [([nums[0]], 1)]

        while len(queue) > 0:
            state, index = queue.pop(0)
            if index == len(nums):
                queue.append((state, index))
                break
            for i in range(len(state) + 1):
                queue.append(([*state[:i], nums[index], *state[i:]], index + 1))

        answer = []
        while len(queue) > 0:
            answer.append(queue.pop(0)[0])

        return answer


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
print(s.permute([1]))