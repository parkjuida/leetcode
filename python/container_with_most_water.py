from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_dict = dict(enumerate(height))
        height_dict = sorted(height_dict.items(), key=lambda x: x[1], reverse=True)

        if height_dict[0][0] < height_dict[1][0]:
            left = 0
            right = 1
        else:
            left = 1
            right = 0

        answer = ((height_dict[right][0] - height_dict[left][0])
                         * min(height_dict[right][1], height_dict[left][1]))
        for i in range(2, len(height_dict)):

            if height_dict[i][0] < height_dict[left][0]:
                left = i
            elif height_dict[i][0] > height_dict[right][0]:
                right = i
            else:
                continue

            answer = max(answer,
                         (height_dict[right][0] - height_dict[left][0])
                         * min(height_dict[right][1], height_dict[left][1])
                         )

        return answer


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))

print(s.maxArea([0, 2]))
