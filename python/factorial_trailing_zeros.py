class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        index = 0
        while index + 5 <= n:
            index += 5
            count = 0
            current_index = index
            while current_index % 5 == 0:
                count += 1
                current_index //= 5
            answer += count

        return answer


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