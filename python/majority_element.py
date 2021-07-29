from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_number = 0

        for num in nums:
            if count == 0:
                majority_number = num
                count += 1
            elif num != majority_number:
                count -= 1
            else:
                count += 1

        return majority_number


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([3]))
print(s.majorityElement([1, 2, 2]))
print(s.majorityElement([2, 1, 2]))
print(s.majorityElement([2, 2, 1]))
print(s.majorityElement([1, 2, 2, 3, 1, 1, 2, 2]))
print(s.majorityElement([6, 6, 6, 7, 7]))