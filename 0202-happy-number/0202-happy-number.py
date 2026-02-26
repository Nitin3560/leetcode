class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            total=0
            temp = n
            while temp>0:
                digit = temp%10
                total += digit*digit
                temp//=10
            n = total
        return n==1