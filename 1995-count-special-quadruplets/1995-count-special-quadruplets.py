class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n=len(nums)
        freq=defaultdict(int)
        ans=0
        for b in range(n-3,0,-1):
            c=b+1
            for d in range(c+1,n):
                freq[nums[d]-nums[c]]+=1
            for a in range(b):
                ans+=freq[nums[a]+nums[b]]
        return ans



