class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = []
        for a, b in intervals:
            if not res or a > res[-1][1]:
                res.append([a, b])
            else:
                if b > res[-1][1]:
                    res[-1][1] = b
        return res
