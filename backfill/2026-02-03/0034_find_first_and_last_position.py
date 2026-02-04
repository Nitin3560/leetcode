class Solution:
    def searchRange(self, nums, target):
        def bound(left):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] > target or (left and nums[m] == target):
                    r = m
                else:
                    l = m + 1
            return l
        l = bound(True)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, bound(False) - 1]
