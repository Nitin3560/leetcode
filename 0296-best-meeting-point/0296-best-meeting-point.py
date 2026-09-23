class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        rows = []
        cols = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        rows.sort()
        cols.sort()

        row_mid = rows[len(rows) // 2]
        col_mid = cols[len(cols) // 2]

        distance = 0

        for r in rows:
            distance += abs(r - row_mid)

        for c in cols:
            distance += abs(c - col_mid)

        return distance