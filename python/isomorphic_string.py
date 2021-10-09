class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for cs, ct in zip(s, t):
            if cs in hash_map_s:
                if hash_map_s[cs] != ct:
                    return False
            if ct in hash_map_t:
                if hash_map_t[ct] != cs:
                    return False
            else:
                hash_map_s[cs] = ct
                hash_map_t[ct] = cs

        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("badc", "baba"))