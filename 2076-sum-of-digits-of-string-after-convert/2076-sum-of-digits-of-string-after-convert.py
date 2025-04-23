class Solution(object):
    def getLucky(self, s, k):
        total = 0
        for char in s:
            num = ord(char) - ord('a') + 1
            while num > 0:
                total += num % 10
                num //= 10
        num = total
        for _ in range(k - 1):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            num = digit_sum
        return num
        