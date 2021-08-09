from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        history = set()
        unique = [0]

        for i in range(1, len(s)):
            for j in unique:
                if s[j] == s[i]:
                    unique.remove(j)
                    history.add(s[i])
                    break
            if s[i] not in history:
                unique.append(i)

        if len(unique) > 0:
            return unique[0]
        else:
            return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
print(s.firstUniqChar("aaabbeabx"))