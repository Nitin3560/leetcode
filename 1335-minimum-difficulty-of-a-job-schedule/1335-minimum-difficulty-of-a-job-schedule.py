class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        memo = {}

        def dp(i, days):
            if days == 1:
                return max(jobDifficulty[i:])

            if (i, days) in memo:
                return memo[(i, days)]

            hardest = 0
            ans = float("inf")

            for j in range(i, n - days + 1):
                hardest = max(hardest, jobDifficulty[j])
                remaining = dp(j + 1, days - 1)
                ans = min(ans, hardest + remaining )
            memo[(i, days)] = ans
            return ans

        return dp(0, d) 