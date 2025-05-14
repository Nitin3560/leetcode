class Solution(object):
    def searchRange(self, nums, target):
        def findBound(isFirst):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (isFirst and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left

        left_index = findBound(True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = findBound(False) - 1
        return [left_index, right_index]
        