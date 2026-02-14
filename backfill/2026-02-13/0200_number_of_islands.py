class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def sink(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != "1":
                    continue
                grid[x][y] = "0"
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    sink(i, j)
        return count
