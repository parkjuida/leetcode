from typing import List
from collections import defaultdict


class Solution:
    def can_be_break(self, logs, current_set):
        if not current_set:
            return True
        for c in current_set:
            if logs[c] != 0:
                return True

        return False

    def partitionLabels(self, s: str) -> List[int]:
        logs = defaultdict(int)

        for c in s:
            logs[c] += 1

        answer = []
        index = 0
        while index < len(s):
            current_set = set()
            length = 0
            while index < len(s) and self.can_be_break(logs, current_set):
                current_set.add(s[index])
                logs[s[index]] -= 1
                length += 1
                index += 1

            answer.append(length)

        return answer



s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("eccbbbbdec"))
print(s.partitionLabels("abb"))