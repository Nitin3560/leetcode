class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        slow= nums[0]
        fast =nums[0]
        while True:
            slow =nums[slow]
            fast =nums[nums[fast]]
            if slow== fast:
                break
        slow = nums[0]
        while slow != fast:
            slow =nums[slow]
            fast =nums[fast]

        return slow