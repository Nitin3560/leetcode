class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        last_added = -1  

        for j, v in enumerate(nums):
            if v == key:
                left = max(0, j - k)
                right = min(n - 1, j + k)

                start = max(left, last_added + 1) 
                for i in range(start, right + 1):
                    ans.append(i)
                last_added = max(last_added, right)

        return ans