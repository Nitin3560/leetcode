class Solution:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            res += [cur + [n] for cur in res]
        return res
