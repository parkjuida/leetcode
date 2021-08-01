from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, count, n = 0, 0, len(nums)
        k = k % n

        while count < n:
            current = (start + k) % n
            current_value = nums[start]
            count += 1

            while current != start:
                nums[current], current_value = current_value, nums[current]
                current = (current + k) % n
                count += 1

            nums[current] = current_value
            start += 1
        return nums


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(s.rotate([-1, -100, 3, 99], 2))
print(s.rotate([1], 1))
print(s.rotate([1, 2], 1))