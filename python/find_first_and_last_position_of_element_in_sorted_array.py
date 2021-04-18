from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        if left >= right:
            return [-1, -1]

        answer = []
        while left < right - 1:
            center = (left + right) // 2
            if nums[center] < target:
                left = center
            else:
                right = center

        if nums[left] == target:
            answer.append(left)
        elif nums[right] == target:
            answer.append(right)
        else:
            answer.append(-1)

        left, right = 0, len(nums) - 1
        while left < right - 1:
            center = (left + right) // 2
            if nums[center] <= target:
                left = center
            else:
                right = center

        if nums[right] == target:
            answer.append(right)
        elif nums[left] == target:
            answer.append(left)
        else:
            answer.append(-1)

        return answer


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([5, 7, 7, 8, 8, 10], 5))
print(s.searchRange([5, 5, 7, 8, 8, 10], 5))
print(s.searchRange([5, 6, 6, 6, 6, 7, 7, 8, 8, 10], 6))
print(s.searchRange([6, 6, 6, 6,], 6))
print(s.searchRange([], 0))
print(s.searchRange([1], 1))
print(s.searchRange([1, 1], 1))
