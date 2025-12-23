class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n

        last = {}
        zeros = []  

        for i, x in enumerate(rains):
            if x == 0:
                zeros.append(i)
                ans[i] = 1 
            else:
                if x in last:
                    j = bisect_right(zeros, last[x])
                    if j == len(zeros):
                        return []
                    dry_day = zeros.pop(j)
                    ans[dry_day] = x 
                last[x] = i
                ans[i] = -1

        return ans