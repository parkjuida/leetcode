from collections import defaultdict
from typing import List


class Solution:
    def is_predecessor(self, candidate, value):
        c_index = 0
        v_index = 0

        while c_index < len(candidate) and v_index < len(value) and candidate[c_index] == value[v_index]:
            c_index += 1
            v_index += 1

        v_index += 1

        while c_index < len(candidate) and v_index < len(value) and candidate[c_index] == value[v_index]:
            c_index += 1
            v_index += 1

        if c_index == len(candidate) and v_index == len(value):
            return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        word_dict = defaultdict(list)

        for word in words:
            word_dict[len(word)].append(word)

        answer = 1
        tree_depth = defaultdict(int)
        for key in sorted(word_dict.keys()):
            if key - 1 not in word_dict:
                for value in word_dict[key]:
                    tree_depth[value] = 1
                continue

            candidates = word_dict[key - 1]
            for value in word_dict[key]:
                for candidate in candidates:
                    if self.is_predecessor(candidate, value):
                        tree_depth[value] = max(tree_depth[value], tree_depth[candidate] + 1)

                if tree_depth[value] == 0:
                    tree_depth[value] = 1

                answer = max(answer, tree_depth[value])

        return answer


s = Solution()
print(s.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(s.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(s.longestStrChain(["abcd", "dbqca"]))
print(s.longestStrChain(["a", "b", "cd", "cdp", "qwer"]))
print(s.longestStrChain(["a"]))
