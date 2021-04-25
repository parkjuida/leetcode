from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            try:
                map_[sorted_s].append(s)
            except KeyError:
                map_[sorted_s] = [s]

        return list(map_.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
