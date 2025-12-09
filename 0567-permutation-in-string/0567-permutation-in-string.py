class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1arr = [0] * 26
        s2arr = [0] * 26

        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if s1arr[i] == s2arr[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')

            if count == 26:
                return True

            s2arr[r] += 1
            if s2arr[r] == s1arr[r]:
                count += 1
            elif s2arr[r] == s1arr[r] + 1:
                count -= 1

            s2arr[l] -= 1
            if s2arr[l] == s1arr[l]:
                count += 1
            elif s2arr[l] == s1arr[l] - 1:
                count -= 1

        return count == 26







