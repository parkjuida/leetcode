class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        operand = 5
        while operand <= n:
            count += n // operand
            operand *= 5

        return count


s = Solution()
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
print(s.trailingZeroes(0))
print(s.trailingZeroes(10))
print(s.trailingZeroes(25))
print(s.trailingZeroes(30))
print(s.trailingZeroes(50))
print(s.trailingZeroes(125))
print(s.trailingZeroes(130))
print(s.trailingZeroes(200))