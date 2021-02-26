class Solution:
    def reverse(self, x: int) -> int:
        ret = ""
        if x < 0:
            ret = "-"
        _x = abs(x)

        while _x != 0 and _x % 10 == 0:
            _x /= 10

        _x = str(int(_x))

        for i in reversed(range(len(_x))):
            ret += _x[i]

        if ret == "" or int(ret) > 2 ** 31 - 1 or int(ret) < -(2 ** 31):
            ret = "0"

        return ret


s = Solution()
print(s.reverse(120))
print(s.reverse(901000))
print(s.reverse(-901000))
print(s.reverse(2**31 + 1))
print(s.reverse(000000000000000000000))
