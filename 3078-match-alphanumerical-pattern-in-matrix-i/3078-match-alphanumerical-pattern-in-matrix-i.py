class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        rows = len(board)
        cols = len(board[0])

        pr = len(pattern)
        pc = len(pattern[0])

        if pr > rows or pc > cols:
            return [-1, -1]

        for r in range(rows - pr + 1):
            for c in range(cols - pc + 1):

                letter_to_digit = {}
                used_digits = {}

                valid = True

                for i in range(pr):
                    for j in range(pc):

                        p = pattern[i][j]
                        value = board[r + i][c + j]

                        if p.isdigit():

                            if int(p) != value:
                                valid = False
                                break

                        else:
                            if p in letter_to_digit:

                                if letter_to_digit[p] != value:
                                    valid = False
                                    break

                            else:
                                if value in used_digits:
                                    valid = False
                                    break

                                letter_to_digit[p] = value
                                used_digits[value] = p

                    if not valid:
                        break

                if valid:
                    return [r, c]

        return [-1, -1]