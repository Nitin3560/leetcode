class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        reversed_int = sign * int(reversed_str)
        return reversed_int if INT_MIN <= reversed_int <= INT_MAX else 0
        