class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        win = 0

        for i in range(minutes):
            win += customers[i] * grumpy[i]

        best = win

        for i in range(minutes, n):
            win += customers[i] * grumpy[i]
            win -= customers[i - minutes] * grumpy[i - minutes]
            best = max(best, win)

        total = best

        for i in range(n):
            total += customers[i] * (1 - grumpy[i])

        return total