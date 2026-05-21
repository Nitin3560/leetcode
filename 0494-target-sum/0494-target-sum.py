class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            newDp = {}

            for total in dp:
                count = dp[total]
                plus = total + num

                if plus not in newDp:
                    newDp[plus] = 0

                newDp[plus] += count
                minus = total - num

                if minus not in newDp:
                    newDp[minus] = 0

                newDp[minus] += count
            dp = newDp

        if target in dp:
            return dp[target]

        return 0