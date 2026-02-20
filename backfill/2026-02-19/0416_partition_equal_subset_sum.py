class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = {0}
        for n in nums:
            dp |= {x + n for x in dp if x + n <= target}
        return target in dp
