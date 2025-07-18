class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        first = nums[:half][::-1]
        last = nums[half:][::-1]
        nums[:] = [0] * n
        nums[::2]=first
        nums[1::2]=last

        return nums