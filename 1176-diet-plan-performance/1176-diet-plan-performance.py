class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        window_sum = sum(calories[:k])
        points = 0
        def score(s: int) -> int:
            if s < lower:
                return -1
            if s > upper:
                return 1
            return 0

        points += score(window_sum)
        for i in range(k, n):
            window_sum += calories[i] - calories[i - k]
            points += score(window_sum)

        return points
