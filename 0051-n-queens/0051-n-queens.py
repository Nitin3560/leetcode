class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        posDiag = set()
        negDiag = set()

        board = []

        for row in range(n):
            board.append(["."] * n)

        def backtrack(row):
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                res.append(solution)
                return

            for col in range(n):
                if col in cols:
                    continue

                if row + col in posDiag:
                    continue

                if row - col in negDiag:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        backtrack(0)

        return res