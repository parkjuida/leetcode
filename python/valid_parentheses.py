class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if not ((c == ")" and t == "(")
                    or (c == "]" and t == "[")
                    or (c == "}" and t == "{")):
                        stack.append(t)
                        stack.append(c)

        if len(stack) == 0:
            return True

        return False


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("]"))
print(s.isValid("["))
print(s.isValid("(])"))