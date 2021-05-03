class Solution:
    def climb(self, n, history):
        print(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        try:
            ret = history[n]
        except KeyError:
            ret = self.climb(n - 1, history) + self.climb(n - 2, history)
            history[n] = ret

        return ret

    def climbStairs(self, n: int) -> int:
        history = {}
        return self.climb(n, history)
