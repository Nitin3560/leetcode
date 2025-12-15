class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n - 2):
            a, b, c = s[i], s[i+1], s[i+2]
            if a != b and a != c and b != c:
                ans += 1
        return ans
