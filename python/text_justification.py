from typing import List

import math


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        prev_index, current_index, words_length = 0, 0, len(words)
        current_len = 0
        current_status = []
        output = []

        while current_index < words_length:
            if current_len + len(words[current_index]) + (current_index - prev_index) > maxWidth:
                space_number = maxWidth - current_len

                for i in range(prev_index, current_index):
                    step = math.ceil(space_number / max((current_index - i - 1), 1))
                    current_status.append(words[i])
                    current_status.append(" " * step)
                    space_number -= step

                output.append("".join(current_status))
                prev_index = current_index
                current_status = []
                current_len = 0
            else:
                current_len += len(words[current_index])
                current_index += 1

        space_number = maxWidth - current_len

        for i in range(prev_index, current_index):
            step = 1
            current_status.append(words[i])
            if space_number != 0:
                current_status.append(" " * step)
            space_number -= step

        current_status.append(" " * space_number)
        output.append("".join(current_status))

        return output


s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(s.fullJustify(words, maxWidth))
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(s.fullJustify(words, maxWidth))

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(s.fullJustify(words, maxWidth))
words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
maxWidth = 16
print(s.fullJustify(words, maxWidth))
