
class Solution:
    def reorganize(self, strings, first):
        answer = [strings[0]]
        n = len(strings)

        for i in range(1, n):
            if strings[i] != strings[i - 1]:
                answer.append(strings[i])
                continue

            j = i + 1
            while j < n and strings[j] == strings[i]:
                j += 1

            if j == n:
                if first:
                    j = n - 1
                else:
                    return ""
            strings[j], strings[i] = strings[i], strings[j]
            answer.append(strings[i])

        return answer

    def reorganizeString(self, s: str) -> str:
        strings = list(s)
        strings = self.reorganize(strings, True)
        if strings == "":
            return strings
        strings = self.reorganize(list(reversed(strings)), False)
        return "".join(strings)


s = Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("aaab"))
print(s.reorganizeString("aabccccddd"))
print(s.reorganizeString("abb"))
print(s.reorganizeString("aabacbbk"))