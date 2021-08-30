from collections import defaultdict
from typing import List


class Solution:
    def is_anagram(self, temp: defaultdict, target: defaultdict):
        for key in target.keys():
            if target[key] != temp[key]:
                return False

        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        target = defaultdict(int)
        for c in p:
            target[c] += 1

        temp = defaultdict(int)
        left = 0
        right = 0
        answer = []
        while right < len(s):
            while right < len(s) and right < left + len(p):
                if s[right] not in p:
                    left = right + 1
                    right = left
                    temp.clear()
                else:
                    temp[s[right]] += 1
                    right += 1

            if right == left + len(p):
                while right < len(s):
                    if self.is_anagram(temp, target):
                        answer.append(left)
                        temp[s[left]] -= 1
                        temp[s[right]] += 1
                        right += 1
                        left += 1
                    else:
                        left += 1
                        right = left
                        temp.clear()
                        break

        if self.is_anagram(temp, target):
            answer.append(left)

        return answer


s = Solution()
print(s.findAnagrams("baa", "aa"))
print(s.findAnagrams("abab", "ab"))
print(s.findAnagrams("cbaebabacd", "abc"))
