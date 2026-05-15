class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result = [[]]

        # for num in nums:
        #     newresult = []
        #     for perm in result:
        #         for i in range(len(perm) + 1):
        #             newresult.append(perm[:i] + [num] + perm[i:])
        #     result = newresult

        # return result
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start] 

        backtrack(0)
        return result