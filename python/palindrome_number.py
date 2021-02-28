class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)

        left = 0
        right = len(string_x) - 1

        while left < right and string_x[left] == string_x[right]:
            left += 1
            right -= 1

        if left >= right:
            return True

        return False



s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(1331))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(-101))