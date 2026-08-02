class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftside = {}
        rightside = {}

        leftsum = 1
        for j in range(n):
            leftside[j] = leftsum 
            leftsum *= nums[j]

        rightsum = 1
        for i in range(n - 1, -1, -1):
            rightside[i] = rightsum  
            rightsum *= nums[i]

        return [leftside[i] * rightside[i] for i in range(n)]
        



