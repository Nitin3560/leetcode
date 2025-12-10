class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res = []
        need = [0] * 26
        win = [0] * 26
        k = len(p)
        
        for c in p:
            need[ord(c) - 97] += 1
        
        for c in s[:k]:
            win[ord(c) - 97] += 1
        
        if win == need:
            res.append(0)
        
        for i in range(k, len(s)):
            win[ord(s[i]) - 97] += 1
            win[ord(s[i - k]) - 97] -= 1
            if win == need:
                res.append(i - k + 1)
        
        return res