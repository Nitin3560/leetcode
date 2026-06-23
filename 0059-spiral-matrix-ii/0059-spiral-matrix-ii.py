class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  

        row = col = 0

        for num in range(1, n * n + 1):
            matrix[row][col] = num

            nr = row + directions[d][0]
            nc = col + directions[d][1]

            if (
                nr < 0 or nr >= n or
                nc < 0 or nc >= n or
                matrix[nr][nc] != 0
            ):
                d = (d + 1) % 4
                nr = row + directions[d][0]
                nc = col + directions[d][1]

            row, col = nr, nc

        return matrix