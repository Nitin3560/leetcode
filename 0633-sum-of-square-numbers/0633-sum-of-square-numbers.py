class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.isqrt(c))

        while left <= right:
            s = left * left + right * right
            if s == c:
                return True
            elif s < c:
                left += 1
            else:
                right -= 1

        return False