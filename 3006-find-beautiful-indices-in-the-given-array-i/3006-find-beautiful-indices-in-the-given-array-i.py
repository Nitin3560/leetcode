class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(text: str, pat: str) -> List[int]:
            m = len(pat)
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pat[i] != pat[j]:
                    j = lps[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                    lps[i] = j

            res = []
            j = 0
            for i, ch in enumerate(text):
                while j > 0 and ch != pat[j]:
                    j = lps[j - 1]
                if ch == pat[j]:
                    j += 1
                    if j == m:
                        res.append(i - m + 1)
                        j = lps[j - 1]
            return res

        A = kmp(s, a)
        B = kmp(s, b)

        ans = []
        for i in A:
            left = i - k
            right = i + k
            pos = bisect_left(B, left)
            if pos < len(B) and B[pos] <= right:
                ans.append(i)
        return ans





