class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            cur = right - left + 1
            if cur > best:
                best = cur
        return best
