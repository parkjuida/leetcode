from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        answer = nums[0]

        while left < right:
            answer = min(answer, nums[left])

            if nums[left] > nums[right]:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid
                    if right - left == 1:
                        answer = min(answer, nums[left], nums[right])
                        break
                else:
                    right = mid
            else:
                break

        return answer


s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11, 13, 15, 17]))
print(s.findMin([1,2,3,4,5]))
print(s.findMin([2,3,4,5,1]))
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,1,2,3]))
print(s.findMin([5,1,2,3,4]))
print(s.findMin([1,2,3,4,5]))