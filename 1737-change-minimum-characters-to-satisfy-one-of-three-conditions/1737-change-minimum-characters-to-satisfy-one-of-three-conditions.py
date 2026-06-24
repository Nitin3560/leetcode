class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        countA = [0] * 26
        countB = [0] * 26

        for ch in a:
            countA[ord(ch) - ord('a')] += 1

        for ch in b:
            countB[ord(ch) - ord('a')] += 1

        n = len(a)
        m = len(b)
        answer = n + m

        for i in range(26):
            changes = (n - countA[i]) + (m - countB[i])
            answer = min(answer, changes)

        prefixA = [0] * 26
        prefixB = [0] * 26

        prefixA[0] = countA[0]
        prefixB[0] = countB[0]

        for i in range(1, 26):
            prefixA[i] = prefixA[i - 1] + countA[i]
            prefixB[i] = prefixB[i - 1] + countB[i]

        for i in range(25):
            changes = (n - prefixA[i]) + prefixB[i]
            answer = min(answer, changes)

            changes = (m - prefixB[i]) + prefixA[i]
            answer = min(answer, changes)

        return answer