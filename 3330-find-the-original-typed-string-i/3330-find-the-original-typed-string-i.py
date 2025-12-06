class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        runs = 1
        for i in range(1, n):
            if word[i] != word[i - 1]:
                runs += 1
        return 1 + n - runs






