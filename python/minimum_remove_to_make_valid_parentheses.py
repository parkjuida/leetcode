class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [-1]
        answer = []
        for index, ch in enumerate(s):
            answer.append(ch)
            if ch == "(":
                stack.append((index, ch))
            if ch == ")":
                if stack[-1] != -1 and stack[-1][1] == "(":
                    stack.pop()
                else:
                    answer.pop()

        index = len(answer) - 1
        while stack[-1] != -1:
            if answer[index] == "(":
                answer.pop(index)
                stack.pop()

            index -= 1

        return "".join(answer)


s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))
print(s.minRemoveToMakeValid("(a(b(c)d)"))
