class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i, x in enumerate(nums):
            if target - x in mp:
                return [mp[target - x], i]
            mp[x] = i
