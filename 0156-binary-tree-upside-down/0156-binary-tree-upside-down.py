# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = None
        prev_right = None
        curr = root

        while curr:
            next_node = curr.left

            curr.left = prev_right
            prev_right = curr.right

            curr.right = prev
            prev = curr

            curr = next_node

        return prev