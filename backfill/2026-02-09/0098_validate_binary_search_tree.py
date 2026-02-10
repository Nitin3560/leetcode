class Solution:
    def isValidBST(self, root):
        def dfs(node, lo, hi):
            if not node:
                return True
            v = node.val
            if (lo is not None and v <= lo) or (hi is not None and v >= hi):
                return False
            return dfs(node.left, lo, v) and dfs(node.right, v, hi)
        return dfs(root, None, None)
