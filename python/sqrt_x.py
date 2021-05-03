class Solution:
    def binary_search(self, left, right, x):
        if right - left == 1 or right == left:
            return left

        mid = (left + right) // 2
        mid_square = mid * mid
        if mid_square < x:
            return self.binary_search(mid, right, x)
        elif mid_square > x:
            return self.binary_search(left, mid, x)
        else:
            return mid

    def mySqrt(self, x: int) -> int:
        temp_x = 1

        while temp_x * temp_x <= x:
            temp_x *= 2

        return self.binary_search(temp_x // 2, temp_x, x)
