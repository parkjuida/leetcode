from typing import List


class Solution:
    def compare(self, word_a, word_b, order_map):
        for a, b in zip(word_a, word_b):
            if order_map[a] < order_map[b]:
                return True
            elif order_map[a] > order_map[b]:
                return False

        if len(word_a) <= len(word_b):
            return True

        return False

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = dict()

        for index, c in enumerate(order):
            order_map[c] = index

        for i in range(len(words) - 1):
            ret = self.compare(words[i], words[i + 1], order_map)
            if ret is False:
                return False

        return True


s = Solution()
print(s.isAlienSorted(["hello", "hello"], "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(s.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))