class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        n = len(s)
        i = 0

        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        digits_found = False
        while i < n and s[i] == '0':
            digits_found = True
            i += 1

        res = 0
        limit = INT_MAX if sign == 1 else 2**31  

        while i < n and s[i].isdigit():
            digits_found = True
            d = ord(s[i]) - ord('0')

            if res > limit // 10 or (res == limit // 10 and d > limit % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + d
            i += 1

        if not digits_found:
            return 0

        ans = sign * res
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
        return ans    