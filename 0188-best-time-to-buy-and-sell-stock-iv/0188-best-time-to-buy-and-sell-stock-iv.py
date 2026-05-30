class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]

            for i in range(1, n):
                dp[t][i] = max(dp[t][i - 1], prices[i] + max_diff)
                max_diff = max( max_diff, dp[t - 1][i] - prices[i])

        return dp[k][n - 1]