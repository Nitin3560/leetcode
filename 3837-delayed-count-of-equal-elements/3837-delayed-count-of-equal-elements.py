class Solution:
    def delayedCount(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # ans = [0] * n
        # freq = defaultdict(int)

        # for i in range(n - 1, -1, -1):
        #     j = i + k + 1
        #     if j < n:
        #         freq[nums[j]] += 1

        #     ans[i] = freq[nums[i]]

        # return ans
        n = len(nums)
        ans = [0] * n
        freq = {}

        for i in range(n - 1, -1, -1):
            j = i + k + 1

            if j < n:
                freq[nums[j]] = freq.get(nums[j], 0) + 1

            ans[i] = freq.get(nums[i], 0)

        return ans