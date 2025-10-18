class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur: list[str], open_used: int, close_used: int):
            if open_used == n and close_used == n:
                res.append("".join(cur))
                return
            if open_used < n:
                cur.append("(")
                dfs(cur, open_used + 1, close_used)
                cur.pop()
            if close_used < open_used:
                cur.append(")")
                dfs(cur, open_used, close_used + 1)
                cur.pop()
        dfs([], 0, 0)
        return res
