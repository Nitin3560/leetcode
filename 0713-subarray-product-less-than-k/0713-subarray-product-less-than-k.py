class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        left = 0
        out = 0
        for right, v in enumerate(nums):
            prod *= v
            while prod >= k:
                prod //= nums[left]
                left += 1
            out += right - left + 1
        return out



