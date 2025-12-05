class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i: int, j: int):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (is_palindrome(left + 1, right) or
                        is_palindrome(left, right - 1))

        return True