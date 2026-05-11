class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        curr = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if len(queue) == 0 or len(queue) == n * n:
            return -1

        while curr < len(queue):
            r, c = queue[curr]
            curr += 1
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        return grid[r][c] - 1