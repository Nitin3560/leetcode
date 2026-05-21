class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (2,1),(2,-1),
            (-2,1),(-2,-1),
            (1,2),(1,-2),
            (-1,2),(-1,-2)
        ]

        dp = [[0] * n for i in range(n)]
        dp[row][column] = 1

        for move in range(k):

            nextDp = [[0] * n for i in range(n)]

            for r in range(n):
                for c in range(n):

                    if dp[r][c] == 0:
                        continue

                    for dr, dc in directions:

                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            nextDp[nr][nc] += dp[r][c] / 8
            dp = nextDp

        return sum(map(sum, dp))