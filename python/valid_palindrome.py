class Solution:
    def is_alpha_numeric(self, c: str):
        return c.isalnum()

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


s = Solution()
print(s.isPalindrome("race a car"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome(".,"))
print(s.isPalindrome("0P"))