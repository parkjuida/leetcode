from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        history = defaultdict(int)
        for c in s:
            history[c] += 1

        for c in t:
            history[c] -= 1

        for v in history.values():
            if v != 0:
                return False

        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))