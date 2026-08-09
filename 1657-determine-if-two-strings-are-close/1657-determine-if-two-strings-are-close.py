class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False

        count1 = [0] * (len(word1) + 1)
        count2 = [0] * (len(word2) + 1)

        for i in range(26):
            count1[freq1[i]] += 1
            count2[freq2[i]] += 1

        for i in range(len(word1) + 1):
            if count1[i] != count2[i]:
                return False

        return True

