class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(sub: str) -> str:
            if len(sub) < 2:
                return ""

            st = set(sub)
            for i, ch in enumerate(sub):
                if ch.swapcase() not in st:
                    left = solve(sub[:i])
                    right = solve(sub[i+1:])
                    if len(left) >= len(right): 
                        return left
                    return right
            return sub 
            
        return solve(s)