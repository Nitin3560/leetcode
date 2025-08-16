class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()            
        ans, path = [], []

        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path.copy())
                return
            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:        
                    break
                path.append(x)        
                dfs(i, remain - x)    
                path.pop()           

        dfs(0, target)
        return ans 