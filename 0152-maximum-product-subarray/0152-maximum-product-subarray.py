class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # ans = nums[0]

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(i, len(nums)):
        #         prod *= nums[j]
        #         ans = max(ans, prod)

        # return ans
        curr_max = curr_min = ans = nums[0]

        for n in nums[1:]:
            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            ans = max(ans, curr_max)

        return ans