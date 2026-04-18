class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ans= False
        # if sorted(s)==sorted(t):
        #     ans= True
        # return ans
        if len(s) != len(t):
            return False
        seen = {}
        freq= {}
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        for ch in t:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        return freq==seen

            