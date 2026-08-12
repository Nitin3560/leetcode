class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def canSplit(maxSum):
            subarrays = 1
            currSum = 0

            for num in nums:
                if currSum + num > maxSum:
                    subarrays += 1
                    currSum = num

                    if subarrays > k:
                        return False
                else:
                    currSum += num

            return True

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left