class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        def backtrack(current: list[int]):
            if len(current) == len(nums):
                results.append(current[:])
                return

            for num in freq:
                if freq[num] > 0:
                    current.append(num)
                    freq[num] -= 1

                    backtrack(current)

                    current.pop()
                    freq[num] += 1

        backtrack([])
        return results