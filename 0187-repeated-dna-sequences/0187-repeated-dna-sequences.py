class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            snippet = s[i:i+10]  
            if snippet in seen:
                repeated.add(snippet)
            else:
                seen.add(snippet)

        return list(repeated)