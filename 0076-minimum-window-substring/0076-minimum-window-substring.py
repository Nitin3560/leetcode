class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        current = {}

        left = 0
        matched = 0
        total = len(need)
        answer = ""

        for right in range(len(s)):
            ch = s[right]

            if ch in current:
                current[ch] += 1
            else:
                current[ch] = 1

            if ch in need and current[ch] == need[ch]:
                matched += 1

            while matched == total:
                window = s[left:right + 1]

                if answer == "" or len(window) < len(answer):
                    answer = window

                left_ch = s[left]
                current[left_ch] -= 1

                if left_ch in need and current[left_ch] < need[left_ch]:
                    matched -= 1

                left += 1

        return answer