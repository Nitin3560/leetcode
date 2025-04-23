class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        candidate = nums[0]
        count = 1
    
        for num in nums[1:]:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        