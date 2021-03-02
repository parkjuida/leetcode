from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        answer = 0

        while left < right:
            answer = max(answer, (right - left) * min(height[right], height[left]))

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return answer


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))

print(s.maxArea([0, 2]))
