from typing import List


class StringNum:
    def __init__(self, num: int):
        self.string_number = str(num)

    def __lt__(self, other):
        this_string = self.string_number
        other_string = other.string_number

        return f"{this_string}{other_string}" > f"{other_string}{this_string}"

    def __len__(self):
        return len(self.string_number)

    def __repr__(self):
        return self.string_number


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_nums = [StringNum(num) for num in nums]
        string_nums.sort()

        if string_nums[0].string_number == "0":
            return "0"

        return "".join([string_num.string_number for string_num in string_nums])


s = Solution()
# print(s.largestNumber([34, 332, 343, 334]))
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([10, 2]))
print(s.largestNumber([1]))
print(s.largestNumber([10]))
print(s.largestNumber([332, 3]))
# print(s.largestNumber([34323, 3432]))
print(s.largestNumber([432, 43243]))
print(s.largestNumber([0, 0]))