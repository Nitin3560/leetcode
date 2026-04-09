class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        queue = [0]
        visited = set([0])
        jumps = 0
        while queue:
            jumps += 1
            next = []
            for i in queue:
                for j in range(1,nums[i]+1):
                    if i+j >= len(nums)-1:
                        return jumps
                    if i+j not in visited:
                        visited.add(i+j)
                        next.append(i+j)
            queue = next
        return jumps