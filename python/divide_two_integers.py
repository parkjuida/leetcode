class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        index = 1

        if dividend * divisor < 0:
            sign = -1
            if dividend < 0:
                dividend *= -1
            else:
                divisor *= -1
        else:
            if dividend < 0 and divisor < 0:
                dividend *= -1
                divisor *= -1

        history = [divisor]
        index_history = [1]
        current = divisor
        cum_index = 0
        while divisor <= dividend:
            if current <= dividend:
                dividend -= current
                current += current
                history.append(current)
                cum_index += index
                index += index
                index_history.append(index)

            else:
                current = history.pop(-1)
                index = index_history.pop(-1)

        answer = cum_index * sign

        return min(answer, 2**31 - 1)


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(0, 1))
print(s.divide(1, 1))
print(s.divide(3, 1))
print(s.divide(-3, 1))
print(s.divide(-1, 1))
print(s.divide(-1, -1))
print(s.divide(-3, -1))
print(s.divide(-10, -1))
print(s.divide(-2147483648, -1), -1)
print(s.divide(-2**31 + 1, -1), -1)
print(s.divide(2**31 - 1, 2), (2**31-1)//2)