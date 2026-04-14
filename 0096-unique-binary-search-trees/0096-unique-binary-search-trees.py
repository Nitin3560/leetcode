class Solution:
    def numTrees(self, n: int) -> int:
        # if n<=1:
        #     return 1
        # total=0
        # for root in range(1,n+1):
        #     left=self.numTrees(root-1)
        #     right=self.numTrees(n-root)
        #     total+=left*right
        # return total
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for root in range(1,i+1):
                dp[i]+=dp[root-1]*dp[i-root]
        return dp[n]