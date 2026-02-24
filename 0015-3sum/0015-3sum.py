# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         ans = set()
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result = tuple(sorted((nums[i], nums[j], nums[k])))
#                         ans.add(result)

#         return [list(t) for t in ans]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n = len(nums)
        ans = set()
        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                if target - nums[j] in seen:
                    result = tuple((nums[i], nums[j], target - nums[j]))
                    ans.add(result)
                seen.add(nums[j])

        return [list(t) for t in ans]