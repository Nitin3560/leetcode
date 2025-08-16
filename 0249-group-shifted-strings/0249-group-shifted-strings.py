class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def key(s: str):
            if len(s) <= 1:
                return ()
            diffs = []
            for i in range(1, len(s)):
                d = (ord(s[i]) - ord(s[i-1])) % 26
                diffs.append(d)
            return tuple(diffs)

        groups = defaultdict(list)
        for s in strings:
            groups[key(s)].append(s)
        return list(groups.values())