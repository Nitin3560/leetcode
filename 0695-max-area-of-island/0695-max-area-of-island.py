class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def sink(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + sink(row+1, col) + sink(row-1, col) + sink(row, col+1) + sink(row, col-1)

        biggest = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    biggest = max(biggest, sink(row, col))

        return biggest