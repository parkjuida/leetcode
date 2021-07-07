class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        answer = []
        carry = 0
        for i in range(1, max(len(num1), len(num2)) + 1):
            try:
                n1 = int(num1[-i])
            except IndexError:
                n1 = 0

            try:
                n2 = int(num2[-i])
            except IndexError:
                n2 = 0

            s = n1 + n2 + carry
            if s > 9:
                carry = 1
                s -= 10
            else:
                carry = 0

            answer.append(str(s))

        if carry > 0:
            answer.append(str(carry))

        return "".join(list(reversed(answer)))


s = Solution()
print(s.addStrings("11", "123"))
print(s.addStrings("456", "77"))
print(s.addStrings("0", "0"))