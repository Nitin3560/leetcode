class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        if m > n:
            s, t = t, s
            m, n = n, m

        i = j = 0
        found_diff = False
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1; j += 1
            else:
                if found_diff:
                    return False
                found_diff = True
                if m == n:
                    i += 1 
                j += 1

        return found_diff if m == n else True