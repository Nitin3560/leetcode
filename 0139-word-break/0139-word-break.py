from os import remove
class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)
        matched = [False] * (n + 1)
        matched[0] = True  

        for i in range(n):
            if not matched[i]:
                continue
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    matched[j] = True

        return matched[n]
