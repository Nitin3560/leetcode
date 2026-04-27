class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            newresult = []
            for perm in result:
                for i in range(len(perm) + 1):
                    newresult.append(perm[:i] + [num] + perm[i:])
            result = newresult

        return result