class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = 0
        _break = False
        prefix = ""

        while True:
            if len(strs) > 0 and len(strs[0]) > common:
                _this = strs[0][common]
            else:
                break

            for _str in strs[1:]:
                if common >= len(_str) or _this != _str[common]:
                    _break = True

            if _break:
                break
            else:
                prefix += strs[0][common]
                common += 1

        return prefix
