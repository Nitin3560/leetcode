class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k=0
        for i in range(len(nums)):
            nums[k]=nums[i]*nums[i]
            k+=1
            
        return sorted(nums)