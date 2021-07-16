class Solution:
    def valid(self, s, left, right, chance):
        while left < right:
            if s[left] != s[right]:
                if chance is True:
                    return False

                ret_left_handled = self.valid(s, left + 1, right, True)
                ret_right_handled = self.valid(s, left, right - 1, True)

                return ret_left_handled or ret_right_handled

            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        return self.valid(s, 0, len(s) - 1, False)


s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abc"))
print(s.validPalindrome("a"))
print(s.validPalindrome("aa"))
