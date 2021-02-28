class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        under_zero = False
        result = ""
        maximum = 2 ** 31 - 1
        minimum = -(2 ** 31)

        while index < len(s) and s[index] == " ":
            index += 1

        if index < len(s) and s[index] == "-":
            under_zero = True

        if index < len(s) and (s[index] == "+" or s[index] == "-"):
            index += 1

        for i in range(index, len(s)):
            if "0" <= s[index] <= "9":
                result += s[index]
                index += 1
            else:
                break

        if result == "":
            result = 0
        else:
            result = int(result)

        if under_zero:
            result *= -1

        if result > maximum:
            result = maximum

        if result < minimum:
            result = minimum

        return result


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("     -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("3.141592"))
print(s.myAtoi("+-12"))
print(s.myAtoi("-+12"))
print(s.myAtoi(""))
print(s.myAtoi("     "))
print(s.myAtoi("+1"))