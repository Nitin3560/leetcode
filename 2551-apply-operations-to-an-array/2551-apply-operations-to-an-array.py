class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr=[]
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        count=0
        for num in nums:
            if num!=0:
                arr.append(num)
            else:
                count+=1
        
        while count>0:
            arr.append(0)
            count-=1

        return arr
