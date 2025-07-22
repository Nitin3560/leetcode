class Solution(object):
    def convert(self, s, numRows):
        r=numRows
        if r == 1 or r >= len(s):
            return s

        v = ['' for _ in range(r)]
        i, d = 0, 1

        for c in s:
            v[i] += c
            if i == 0:
                d = 1
            elif i == r - 1:
                d = -1
            i += d

        return ''.join(v)




        