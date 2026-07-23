# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def dfs(node, direction, length):
            if node is None:
                return

            if length > self.answer:
                self.answer = length

            if direction == 0:
                dfs(node.left, 0, 1)
                dfs(node.right, 1, length + 1)
                
            else:
                dfs(node.right, 1, 1)
                dfs(node.left, 0, length + 1)

        if root is None:
            return 0

        dfs(root.left, 0, 1)
        dfs(root.right, 1, 1)

        return self.answer