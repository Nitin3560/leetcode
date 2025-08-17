class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        prev = lower - 1 

        for curr in nums + [upper + 1]:
            start = prev + 1
            end = curr - 1
            if start <= end:
                res.append([start, end])
            prev = curr

        return res            