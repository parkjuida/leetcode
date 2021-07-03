from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timetable = []
        start, end = "S", "E"
        for interval in intervals:
            timetable.append((interval[0], start))
            timetable.append((interval[1], end))

        timetable = sorted(timetable, key=lambda x: (x[0], x[1]))
        count = 0
        max_count = 0
        for _, type in timetable:
            if type == start:
                count += 1
            else:
                count -= 1

            max_count = max(max_count, count)

        return max_count


s = Solution()
print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(s.minMeetingRooms([[7, 10], [2, 4]]))
print(s.minMeetingRooms([[13, 15], [1, 13]]))