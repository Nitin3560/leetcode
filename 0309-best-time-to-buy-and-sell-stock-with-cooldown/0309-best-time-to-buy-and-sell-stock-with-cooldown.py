class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # if i >= n:
        #     return 0
        # if hold:
        #     sell = prices[i] + max_profit(prices,i+2, 0)
        #     skip = maxp_rofit(prices,i+1, 1)
        #     return sell if sell > skip else skip
        # else:
        #     buy = -prices[i] + max_profit(prices,i+1, 1)
        #     skip = max_profit(prices,i+1, 0)
        #     return buy if buy > skip else skip
        held = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prevsold = sold       
            sold = held + price
            held = max(held, rest - price)
            rest = max(rest, prevsold)

        return max(sold, rest)