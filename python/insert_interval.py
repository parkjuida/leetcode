from typing import List


class Solution:
    def merge(self, interval_a, interval_b):
        return [min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1])]

    def overlay(self, interval_a, interval_b):
        return interval_a[0] <= interval_b[1] and interval_b[0] <= interval_a[1]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []

        index = 0
        while index < len(intervals) and intervals[index][0] < newInterval[0]:
            index += 1

        intervals.insert(index, newInterval)

        index = 0
        current = intervals[index]

        while index < len(intervals) - 1:
            if self.overlay(current, intervals[index + 1]):
                current = self.merge(current, intervals[index + 1])
            else:
                answer.append(current)
                current = intervals[index + 1]
            index += 1

        answer.append(current)

        return answer


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(s.insert([], [5, 7]))
print(s.insert([[1, 5]], [2, 3]))
print(s.insert([[1, 5]], [2, 7]))
print(s.insert([[1, 5]], [6, 8]))
print(s.insert([[6, 8]], [1, 5]))
print(s.insert([[6, 8], [9, 10]], [1, 5]))
print(s.insert([[4, 8], [9, 10]], [1, 5]))