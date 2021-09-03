

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][1] + 1 == k and stack[-1][0] == c:
                while stack and stack[-1][0] == c:
                    stack.pop()
                continue
            if stack and stack[-1][0] == c:
                number_of_prev_same_char = stack[-1][1] + 1
            else:
                number_of_prev_same_char = 1
            stack.append((c, number_of_prev_same_char))

        answer = [s[0] for s in stack]
        return "".join(answer)


s = Solution()
print(s.removeDuplicates("aadbbccbdefsdfabbafdsfedbc", 2))
print(s.removeDuplicates("abbccddddccbb", 4))
print(s.removeDuplicates("deeedbbcccbdaa", 3))
print(s.removeDuplicates("pbbcggttciiippooaais", 2))
