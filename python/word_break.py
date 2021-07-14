from typing import List


class Solution:
    def find(self, index, s, wordDict, history):
        if index >= len(s):
            return True

        if history[index] is False:
            return False

        for word in wordDict:
            l = len(word)
            if s[index:index + l] == word:
                ret = self.find(index + len(word), s, wordDict, history)
                if ret is True:
                    return True

        history[index] = False
        return history[index]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        history = [None] * len(s)
        return self.find(0, s, wordDict, history)


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))