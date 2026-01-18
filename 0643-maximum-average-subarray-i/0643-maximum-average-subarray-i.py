class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window=sum(nums[:k])
        maxans=window
        for i in range(k,n):
            window+=nums[i]
            window-=nums[i-k]
            maxans=max(maxans,window)
        return maxans/k

