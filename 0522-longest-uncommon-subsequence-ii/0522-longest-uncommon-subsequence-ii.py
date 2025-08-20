class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a: str, b: str) -> bool:
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
                    if i == len(a):
                        return True
            return i == len(a)

        freq = Counter(strs)
        strs_sorted = sorted(strs, key=len, reverse=True)
        longer = []

        for s in strs_sorted:
            if freq[s] == 1:
                if not any(len(t) > len(s) and is_subseq(s, t) for t in longer):
                    return len(s)
            longer.append(s)
        return -1