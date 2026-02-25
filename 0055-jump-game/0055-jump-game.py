# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n=len(nums)
#         if n<=2 and nums[0]>= (n-1):
#             return True 
#         if nums[0]==0:
#             return False
#         k=n-1

#         ans = False 
#         for i in range(n-2,0,-1):
#             while ans is False and nums[i] >= (k - i):
#                 ans = True
#                 k-=1
         
#         return ans

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(goal - 1, -1, -1):
            if i + nums[i] >=  goal:
                goal = i
        return goal == 0