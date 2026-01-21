class Solution:
    def maxProfit(self, prices):
        mn = 10**18
        ans = 0
        for p in prices:
            if p < mn:
                mn = p
            else:
                if p - mn > ans:
                    ans = p - mn
        return ans
