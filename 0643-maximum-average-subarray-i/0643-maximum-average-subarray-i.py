class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        best_sum = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            if cur_sum > best_sum:
                best_sum = cur_sum
        return best_sum / k

