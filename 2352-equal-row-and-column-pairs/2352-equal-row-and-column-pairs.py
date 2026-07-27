class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        
        for i in range(n):
            for j in range(n):
                col = []
                for k in range(n):
                    col.append(grid[k][j])
                
                equal = True
                for k in range(n):
                    if grid[i][k] != col[k]:
                        equal = False
                        break
                
                if equal:
                    count += 1
        
        return count