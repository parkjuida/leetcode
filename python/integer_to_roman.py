class Solution:
    def intToRoman(self, num: int) -> str:
        digit_num = {
            1000: ["M", "M", "M"],
            100: ["C", "D", "M"],
            10: ["X", "L", "C"],
            1: ["I", "V", "X"]
        }
        digit_map = {}
        for index in digit_num:
            digit_map[index] = {
                9: digit_num[index][0] + digit_num[index][2],
                8: digit_num[index][1] + digit_num[index][0] * 3,
                7: digit_num[index][1] + digit_num[index][0] * 2,
                6: digit_num[index][1] + digit_num[index][0] * 1,
                5: digit_num[index][1],
                4: digit_num[index][0] + digit_num[index][1],
                3: digit_num[index][0] * 3,
                2: digit_num[index][0] * 2,
                1: digit_num[index][0] * 1,
            }

        index = 1000
        ret = ""
        while num > 0:
            split = num // index
            num = num % index

            if split != 0:
                ret += digit_map[index][split]

            index = index // 10

        return ret

s = Solution()
print(s.intToRoman(1))
print(s.intToRoman(10))
print(s.intToRoman(101))
print(s.intToRoman(1000))
print(s.intToRoman(3999))
print(s.intToRoman(3888))
print(s.intToRoman(1994))
print(s.intToRoman(58))
