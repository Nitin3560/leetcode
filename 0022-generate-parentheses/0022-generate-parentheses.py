class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def bt(s, o, c):
            if len(s) == 2 * n:
                res.append(s)
                return
            if o < n:
                bt(s + '(', o + 1, c)
            if c < o:
                bt(s + ')', o, c + 1)

        bt('', 0, 0)
        return res
        