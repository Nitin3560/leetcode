class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        cur = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                cur = 0
                continue

            if i == 0 or nums[i - 1] > threshold or (nums[i] % 2) == (nums[i - 1] % 2):
                cur = 1 if nums[i] % 2 == 0 else 0
            else:
                cur += 1
            ans = max(ans, cur)

        return ans