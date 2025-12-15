class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        max_freq = 0
        ans = 0

        for r, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])

            while (r - l + 1) - max_freq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans