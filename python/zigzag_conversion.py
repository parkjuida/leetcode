class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = ""

        if numRows == 1:
            return s

        for i in range(1, numRows + 1):
            interval = (numRows - i) * 2, (i - 1) * 2
            index = i - 1
            counter = 0
            while index < len(s):
                if interval[counter] != 0:
                    ret += s[index]
                index += interval[counter]
                counter = not counter

        return ret


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("PAYPALISHIRING", 5))
print(s.convert("A", 1))
