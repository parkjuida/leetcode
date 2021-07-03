class Solution:
    def get_number(self, stack, minus):
        number = 0
        if type(stack[-1]) is not str or stack[-1] < '0' or stack[-1] > '9':
            return

        odd = 1
        while '0' <= stack[-1] <= '9':
            number += int(stack.pop()) * odd
            odd *= 10
        else:
            stack.append(minus * number)

    def calculate(self, s: str) -> int:
        stack = ['(']
        minus = 1
        for c in s:
            if c == " ":
                self.get_number(stack, minus)
                continue
            elif c == "(":
                stack.append(c)
            elif c == "+":
                if stack[-1] != "+" or stack[-1] != "-":
                    self.get_number(stack, minus)
                    stack.append(c)
            elif c == "-":
                if stack[-1] == "+" or stack[-1] == "-":
                    minus = -1
                else:
                    self.get_number(stack, minus)
                    stack.append(c)
            elif c == ")":
                self.get_number(stack, minus)
                self.calc(stack)
            else:
                stack.append(c)

        self.get_number(stack, minus)
        self.calc(stack)
        return stack.pop()

    def calc(self, stack):
        partial_sum = 0
        temp_number = None
        while stack[-1] != "(":
            temp = stack.pop()
            if temp == "-":
                partial_sum += -1 * temp_number
                temp_number = None
            elif temp == "+":
                partial_sum += temp_number
                temp_number = None
            else:
                temp_number = temp
        if temp_number is not None:
            partial_sum += temp_number
        stack.pop()
        stack.append(partial_sum)
