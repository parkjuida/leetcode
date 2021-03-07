class Solution:
    def romanToInt(self, s: str) -> int:
        candidates = [
            {
                "DCCC": 800,
                "LXXX": 80,
                "VIII": 8,
                },
            {
                "MMM": 3000,
                "DCC": 700,
                "CCC": 300,
                "LXX": 70,
                "XXX": 30,
                "VII": 7,
                "III": 3,
                },
            {
                "MM": 2000,
                "CM": 900,
                "DC": 600,
                "CD": 400,
                "CC": 200,
                "XC": 90,
                "LX": 60,
                "XL": 40,
                "XX": 20,
                "IX": 9,
                "VI": 6,
                "IV": 4,
                "II": 2
                },
            {
                "M": 1000,
                "D": 500,
                "C": 100,
                "L": 50,
                "X": 10,
                "V": 5,
                "I": 1,
                },
        ]

        index = 0
        answer = 0
        while index < len(s):
            for length, candidate in enumerate(candidates):
                try:
                    answer += candidate[s[index: index + (4 - length)]]
                    index += (4 - length)
                    break
                except KeyError:
                    pass

        return answer

