class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        res = n
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            keep = right - left + 1
            res = min(res, n - keep)
        return res



