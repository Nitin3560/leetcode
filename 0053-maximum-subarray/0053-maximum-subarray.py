class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=c=nums[0]
        for x in nums[1:]:
            c=max(x,c+x)
            m=max(m,c)
        return m



