class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if abs(curr - target) < abs(best - target):
                    best = curr
                if curr == target:
                    return target
                if curr < target:
                    l += 1
                else:
                    r -= 1
        return best
        