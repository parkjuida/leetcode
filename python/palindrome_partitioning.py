from typing import List


class Solution:
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def break_up(self, s, left, right):
        if left > right:
            return []

        answer = []
        for i in range(left, right + 1):
            if self.is_palindrome(s, left, i):
                ret = self.break_up(s, i + 1, right)
                if not ret:
                    answer.append([s[left:i + 1]])
                if ret is not None:
                    for r in ret:
                        answer.append([s[left:i + 1], *r])

        return answer

    def partition(self, s: str) -> List[List[str]]:
        return self.break_up(s, 0, len(s) - 1)


s = Solution()
print(s.partition("aab"))
print(s.partition("ababa"))