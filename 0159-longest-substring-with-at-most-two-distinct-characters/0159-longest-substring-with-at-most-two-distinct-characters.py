class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        freq = {}
        best = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

            while len(freq) > 2:
                left_ch = s[left]
                freq[left_ch] -= 1
                if freq[left_ch] == 0:
                    del freq[left_ch]
                left += 1

            best = max(best, right - left + 1)

        return best