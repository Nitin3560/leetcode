class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            total = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1