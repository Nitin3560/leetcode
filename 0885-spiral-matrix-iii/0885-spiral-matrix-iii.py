class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        r, c = rStart, cStart
        step = 1
        d = 0

        if 0 <= r < rows and 0 <= c < cols:
            res.append([r, c])

        while len(res) < rows * cols:
            for _ in range(2):  
                dr, dc = directions[d]

                for _ in range(step):
                    r += dr
                    c += dc

                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])

                    if len(res) == rows * cols:
                        return res

                d = (d + 1) % 4

            step += 1

        return res