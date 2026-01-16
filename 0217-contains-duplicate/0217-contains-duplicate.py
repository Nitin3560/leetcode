class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        ans=False
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                ans=True
        return ans

    