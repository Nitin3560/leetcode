class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        count=0
        n=len(nums)-1
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
            else:
                count+=1
        
        while count>0:
            nums[n]=0
            n-=1
            count-=1
        
        return nums
                
        