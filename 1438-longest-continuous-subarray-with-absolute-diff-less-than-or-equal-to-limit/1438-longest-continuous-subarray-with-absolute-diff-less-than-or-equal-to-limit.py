class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxD=deque();minD=deque();l=0;ans=0
        for r,x in enumerate(nums):
            while maxD and maxD[-1]<x:maxD.pop()
            while minD and minD[-1]>x:minD.pop()
            maxD.append(x);minD.append(x)
            while maxD[0]-minD[0]>limit:
                if nums[l]==maxD[0]:maxD.popleft()
                if nums[l]==minD[0]:minD.popleft()
                l+=1
            ans=max(ans,r-l+1)
        return ans



