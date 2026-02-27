class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        inc=[1]*n
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                inc[i]=inc[i+1]+1
        def ok(k):
            for a in range(n-2*k+1):
                if inc[a]>=k and inc[a+k]>=k:
                    return True
            return False
        lo,hi=0,n//2
        while lo<hi:
            mid=(lo+hi+1)//2
            if ok(mid):
                lo=mid
            else:
                hi=mid-1
        return lo