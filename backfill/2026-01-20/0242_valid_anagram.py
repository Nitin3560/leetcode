class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
        for ch in t:
            if ch not in cnt:
                return False
            v = cnt[ch] - 1
            if v == 0:
                del cnt[ch]
            else:
                cnt[ch] = v
        return len(cnt) == 0
