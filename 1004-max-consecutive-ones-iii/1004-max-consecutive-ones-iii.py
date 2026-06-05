class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left = 0
        # used = 0
        # length = 0

        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         used += 1

        #     while used > k:
        #         if nums[left] == 0:
        #             used -= 1
        #         left += 1

        #     length = max(length, right - left + 1)

        # return length

        left = 0
        zeros = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        return best