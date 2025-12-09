class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        extra = 0
        cur = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
            else:
                cur += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                cur -= customers[i - minutes]
            if cur > extra:
                extra = cur
        return base + extra