class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(x):
            if x < 0:
                return 0
            left = 0
            s = 0
            res = 0
            for right, v in enumerate(nums):
                s += v
                while s > x:
                    s -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        return at_most(goal) - at_most(goal - 1)