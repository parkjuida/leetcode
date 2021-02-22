class Solution:
    def find(self, s, start):
        left = int(start)
        right = round(start + 0.1)

        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1

        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s) * 2):
            answer = self.find(s, i / 2)

            if len(longest) < len(answer):
                longest = answer

        return longest


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("aaaa"))
print(s.longestPalindrome("bb"))