class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 1:
            return len(s)

        n = len(s)
        ans = 0

        for target_unique in range(1, 27):
            freq = [0] * 26
            l = 0
            unique = 0
            at_least_k = 0

            for r in range(n):
                idx = ord(s[r]) - 97
                if freq[idx] == 0:
                    unique += 1
                freq[idx] += 1
                if freq[idx] == k:
                    at_least_k += 1

                while unique > target_unique:
                    idxl = ord(s[l]) - 97
                    if freq[idxl] == k:
                        at_least_k -= 1
                    freq[idxl] -= 1
                    if freq[idxl] == 0:
                        unique -= 1
                    l += 1

                if unique == target_unique and at_least_k == target_unique:
                    ans = max(ans, r - l + 1)

        return ans