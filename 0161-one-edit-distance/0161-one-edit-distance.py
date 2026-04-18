class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # m, n = len(s), len(t)
        # if abs(m - n) > 1:
        #     return False
        # if m > n:
        #     s, t = t, s
        #     m, n = n, m

        # i = j = 0
        # found_diff = False
        # while i < m and j < n:
        #     if s[i] == t[j]:
        #         i += 1; j += 1
        #     else:
        #         if found_diff:
        #             return False
        #         found_diff = True
        #         if m == n:
        #             i += 1 
        #         j += 1

        # return found_diff if m == n else True
        if abs(len(s)-len(t))>1:
            return False
        if len(s)==len(t):
            diff=0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff+=1
            return diff==1
        s1=s if len(s)<len(t) else t
        s2=s if len(s)>len(t) else t
        i1, i2=0, 0
        diff=0
        while i1<len(s1) and i2<len(s2):
            if s1[i1] != s2[i2]:
                diff+=1
                if diff>1:
                    return False
                i2+=1
            else:
                i1+=1
                i2+=1
        return True