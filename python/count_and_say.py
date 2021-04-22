class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev_string = self.countAndSay(n - 1)

        answer = []
        digit = prev_string[0]
        count = 1
        for c in prev_string[1:]:
            if c == digit:
                count += 1
            else:
                answer.append(str(count))
                answer.append(digit)

                digit = c
                count = 1

        answer.append(str(count))
        answer.append(digit)

        return "".join(answer)
