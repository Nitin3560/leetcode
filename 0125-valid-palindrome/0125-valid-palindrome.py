class Solution(object):
    def isPalindrome(self, s):
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        if filtered == filtered[::-1]:
            return True
        else:
            return False