class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left, right = 0, len(num) - 1

        while left < right:
            lv, rv = num[left], num[right]
            if not (
                    (lv == rv and lv in ["0", "1", "8"])
                    or (lv == '6' and rv == '9')
                    or (lv == '9' and rv == '6')
            ):
                return False

            left += 1
            right -= 1

        if (left == right) and (num[left] not in ["0", "1", "8"]):
            return False

        return True


s = Solution()
print(s.isStrobogrammatic("69"))
print(s.isStrobogrammatic("88"))
print(s.isStrobogrammatic("692"))
print(s.isStrobogrammatic("1"))
print(s.isStrobogrammatic("2"))
print(s.isStrobogrammatic("101"))