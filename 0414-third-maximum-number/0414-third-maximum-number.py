class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = 3
        seen = set()
        arr = sorted(nums, reverse=True)

        for num in arr:
            if num not in seen:
                seen.add(num)
                count -= 1 
                if count == 0:
                    return num

        return max(seen)
                