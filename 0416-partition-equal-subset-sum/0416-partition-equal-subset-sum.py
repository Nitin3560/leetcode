class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        reachable = {0}
        for x in nums:
            new = set()
            for s in reachable:
                ns = s + x
                if ns == target:
                    return True
                if ns < target:
                    new.add(ns)
            reachable |= new
        return (target in reachable)