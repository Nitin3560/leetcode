class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            x = abs(nums[i])
            index = x - 1

            if nums[index] < 0:
                ans.append(x)
            else:
                nums[index] = -nums[index]

        return ans