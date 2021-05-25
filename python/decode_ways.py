class Solution:
    def find(self, s, index, history):
        if index < len(s) and s[index] == "0":
            return 0
        if index >= len(s) or (index == len(s) - 1 and s[index] != "0"):
            return 1
        if index in history:
            return history[index]

        ret = 0
        if s[index] == "1":
            ret += self.find(s, index + 2, history)
        if s[index] == "2":
            if int(s[index + 1]) < 7:
                ret += self.find(s, index + 2, history)
        if index + 1 < len(s):
            ret += self.find(s, index + 1, history)

        history[index] = ret
        return ret

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        history = {}
        return self.find(s, 0, history)


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("0"))
print(s.numDecodings("06"))
print(s.numDecodings("1"))
print(s.numDecodings("26"))
print(s.numDecodings("10"))
print(s.numDecodings("2101"))
print(s.numDecodings("1" * 100))