class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        mx = [[0] * n for _ in range(n)]
        for i in range(n):
            mx[i][i] = arr[i]
            for j in range(i + 1, n):
                mx[i][j] = max(mx[i][j-1], arr[j])

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):    
            for i in range(n - length + 1):  
                j = i + length - 1  
                dp[i][j] = float('inf')
                for k in range(i, j):      
                    cost = dp[i][k] + dp[k+1][j] + mx[i][k] * mx[k+1][j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n-1]