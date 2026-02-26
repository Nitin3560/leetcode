# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
#         while n!=1 and n not in seen:
#             seen.add(n)
#             total=0
#             temp = n
#             while temp>0:
#                 digit = temp%10
#                 total += digit*digit
#                 temp//=10
#             n = total
#         return n==1

class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1