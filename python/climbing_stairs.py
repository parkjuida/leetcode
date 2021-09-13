class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 2
        prev_prev = 1
        for i in range(3, n + 1):
            temp = prev
            prev = prev + prev_prev
            prev_prev = temp

        return prev


s = Solution()
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))