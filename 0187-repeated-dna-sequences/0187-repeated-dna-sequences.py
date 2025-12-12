class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        if len(s) < L:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - L + 1):
            sub = s[i:i+L]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)

        return list(repeated)