class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            c = Counter(nums[i:i+k])
            a = sorted(c.items(), key=lambda p: (p[1], p[0]), reverse=True)
            s = 0
            for j in range(min(x, len(a))):
                v, f = a[j]
                s += v * f
            res.append(s)
        return res