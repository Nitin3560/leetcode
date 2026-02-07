class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        start = 0
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                tmp = [cur + [n] for cur in res[start:]]
            else:
                tmp = [cur + [n] for cur in res]
            start = len(res)
            res += tmp
        return res
