class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("  fly me to the moon   "))