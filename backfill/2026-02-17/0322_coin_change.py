class Solution:
    def coinChange(self, coins, amount):
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            best = INF
            for c in coins:
                if a - c >= 0:
                    v = dp[a - c] + 1
                    if v < best:
                        best = v
            dp[a] = best
        return -1 if dp[amount] == INF else dp[amount]
