class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result = []

        # for i in range(len(nums) - k + 1):
        #     window = nums[i]

        #     for j in range(i, i + k):
        #         if nums[j] > window:
        #             window = nums[j]

        #     result.append(window)

        # return result

        queue = []
        start = 0
        result = []

        for i in range(len(nums)):

            while len(queue) > start and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            if queue[start] <= i - k:
                start += 1

            if i >= k - 1:
                result.append(nums[queue[start]])

        return result