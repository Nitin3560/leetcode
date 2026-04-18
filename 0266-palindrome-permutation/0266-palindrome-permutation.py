class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = {}
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        odd=0
        for val in seen.values():
            if val % 2 != 0:
                odd+=1
        return True if odd < 2 else False
