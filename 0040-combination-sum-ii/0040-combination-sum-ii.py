class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0:
                return

            prev = None
            for i in range(start, len(candidates)):
                x = candidates[i]
                if prev is not None and x == prev:
                    continue
                if x > remain: 
                    break
                path.append(x)
                dfs(i + 1, remain - x) 
                path.pop()
                prev = x

        dfs(0, target)
        return res