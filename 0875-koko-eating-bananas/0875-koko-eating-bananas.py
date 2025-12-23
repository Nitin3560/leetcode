class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k: int) -> int:
            return sum((p + k - 1) // k for p in piles)

        left, right=1, max(piles)
        while left<right:
            mid = (left+right)//2
            if hours_needed(mid) <=h:
                right = mid
            else:
                left = mid+1  
        return left