class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        log_k = math.log(k)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        count = 0
        n = len(prefix)

        for i in range(n):
            left, right = i + 1, n
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] < prefix[i] + log_k - 1e-9:
                    left = mid + 1
                else:
                    right = mid
            count += left - i - 1

        return count