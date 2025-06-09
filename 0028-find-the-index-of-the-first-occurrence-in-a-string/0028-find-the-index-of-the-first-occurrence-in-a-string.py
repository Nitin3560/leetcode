class Solution(object):
    def strStr(self, haystack, needle):
        length_h, length_n = len(haystack), len(needle)
    
        for i in range(length_h - length_n + 1):
            if haystack[i:i+length_n] == needle:
                return i
        return -1