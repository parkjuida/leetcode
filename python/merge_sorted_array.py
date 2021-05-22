from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index, nums2_index = 0, 0
        answer = []

        while nums1_index < m and nums2_index < n:
            if nums1[nums1_index] < nums2[nums2_index]:
                answer.append(nums1[nums1_index])
                nums1_index += 1
            else:
                answer.append(nums2[nums2_index])
                nums2_index += 1

        while nums1_index < m:
            answer.append(nums1[nums1_index])
            nums1_index += 1

        while nums2_index < n:
            answer.append(nums2[nums2_index])
            nums2_index += 1

        for index, value in enumerate(answer):
            nums1[index] = value


s = Solution()
a = [1, 2, 3, 0, 0, 0]
s.merge(a, 3, [2, 5, 6], 3)
print(a)
a = [2, 5, 7, 8, 0, 0, 0]
s.merge(a, 4, [2, 4, 5], 3)
print(a)
