class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue

                if i == m - 1:
                    need = dp[i][j + 1]
                elif j == n - 1:
                    need = dp[i + 1][j]
                else:
                    need = min(dp[i + 1][j], dp[i][j + 1])

                dp[i][j] = max(1, need - dungeon[i][j])

        return dp[0][0]