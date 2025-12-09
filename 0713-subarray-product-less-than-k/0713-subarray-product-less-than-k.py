class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        lk = math.log(k)
        pre = [0.0]
        for x in nums:
            pre.append(pre[-1] + math.log(x))

        ans = 0
        m = len(pre)

        for i in range(m):
            lo, hi = i + 1, m
            while lo < hi:
                mid = (lo + hi) // 2
                if pre[mid] < pre[i] + lk - 1e-9:
                    lo = mid + 1
                else:
                    hi = mid
            ans += lo - i - 1

        return ans