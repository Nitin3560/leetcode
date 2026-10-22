class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        k = nums.index(0)
        ans = float('inf')

        increasing = all(
            nums[(i + 1) % n] == (nums[i] + 1) % n
            for i in range(n)
        )

        decreasing = all(
            nums[(i + 1) % n] == (nums[i] - 1) % n
            for i in range(n)
        )

        if increasing:
            ans = min(ans, k, n - k + 2)

        if decreasing:
            ans = min(ans, k + 2, n - k)

        return -1 if ans == float('inf') else ans
