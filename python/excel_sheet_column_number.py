class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        unit = ord('Z') - ord('A') + 1
        for c in columnTitle:
            answer *= unit
            answer += ord(c) - ord('A') + 1

        return answer

s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))
print(s.titleToNumber("FXSHRXW"))