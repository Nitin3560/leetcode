class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                dp[left][right] = float('inf')
                for mid in range(left + 1, right):
                    cost = values[left] * values[mid] * values[right]
                    total = cost + dp[left][mid] + dp[mid][right]
                    if total < dp[left][right]:
                        dp[left][right] = total

        return dp[0][n - 1]