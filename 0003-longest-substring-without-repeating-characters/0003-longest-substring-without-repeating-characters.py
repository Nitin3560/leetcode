class Solution(object):
    def lengthOfLongestSubstring(self,s):
        x = len(s)
        max_len = 0
        for i in range(x):
            cur_len = 1
            for j in range(i + 1, x):
                duplicate = False
                for k in range(i, j):
                    if s[k] == s[j]:
                        duplicate = True
                        break
                if duplicate:
                    break
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len



        