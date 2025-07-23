class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s) == Counter(t)