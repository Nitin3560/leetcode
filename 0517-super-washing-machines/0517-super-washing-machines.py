class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)

        if total % n != 0:
            return -1

        target = total // n

        balance = 0
        ans = 0

        for dresses in machines:
            diff = dresses - target
            balance += diff
            ans = max(ans, abs(balance), diff)

        return ans