class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = {}

        i = j = 0
        max_length = -1

        while j != len(s):
            if characters.get(s[j], -1) > -1:
                for k in range(i, characters[s[j]]):
                    del characters[s[k]]
                i = characters[s[j]] + 1

            characters[s[j]] = j
            j += 1
            max_length = max(max_length, j - i)

        max_length = max(max_length, j - i)

        return max_length

s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring("vdvf"))
print(s.lengthOfLongestSubstring("abba"))


