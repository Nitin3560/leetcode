class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)
        start = 0

        for end in range(len(s) + 1):
            if end == len(s) or s[end] == " ":
                self.reverse(s, start, end - 1)
                start = end + 1

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        