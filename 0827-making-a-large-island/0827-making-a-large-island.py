class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = {}

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(row, col, island_id):
            if (
                row < 0 or row >= n or
                col < 0 or col >= n or
                grid[row][col] != 1
            ):
                return 0

            grid[row][col] = island_id

            size = 1

            for dr, dc in directions:
                size += dfs(row + dr, col + dc, island_id)

            return size

        island_id = 2

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    size = dfs(row, col, island_id)
                    area[island_id] = size
                    island_id += 1

        answer = max(area.values(), default=0)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:

                    new_size = 1
                    seen = set()

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (
                            0 <= new_row < n and
                            0 <= new_col < n
                        ):
                            neighbor_id = grid[new_row][new_col]

                            if neighbor_id > 1 and neighbor_id not in seen:
                                seen.add(neighbor_id)
                                new_size += area[neighbor_id]

                    answer = max(answer, new_size)

        return answer