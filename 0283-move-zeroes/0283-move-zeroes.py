# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
        # n = len(nums)
        # for i in range(n):
        #     if nums[i]!= 0:
        #         k = i
        #         while k > 0 and nums[k - 1] == 0:
        #             nums[k], nums[k - 1]= nums[k - 1], nums[k]    
        #             k-= 1
        # return nums                  

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for j in range(k, n):
            nums[j] = 0
        
        return nums
                
        