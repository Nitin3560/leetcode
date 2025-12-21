class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        def h(i,m):
            l=2*i+1
            r=2*i+2
            g=i
            if l<m and nums[l]>nums[g]:
                g=l
            if r<m and nums[r]>nums[g]:
                g=r
            if g!=i:
                nums[i],nums[g]=nums[g],nums[i]
                h(g,m)
        for i in range(n//2-1,-1,-1):
            h(i,n)
        for i in range(n-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            h(0,i)
        return nums