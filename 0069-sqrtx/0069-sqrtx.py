class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        y = x
        while y * y > x:
            y = (y + x // y) // 2
        return y