class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        best = values[0]
        ans = float('-inf')

        for j in range(1, len(values)):
            score = best + values[j] - j 
            ans = max(ans, score)

            best = max(best, values[j] + j)

        return ans 