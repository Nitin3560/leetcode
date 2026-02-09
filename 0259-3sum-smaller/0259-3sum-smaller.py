class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n<3:
            return 0
        nums.sort()
        count=0
        for i in range(n-2):
            l,r=i+1,n-1
            while l < r:
                s=nums[i]+nums[l]+nums[r]
                if s<target:
                    count+=(r-l)   
                    l+=1
                else:
                    r-=1
        return count