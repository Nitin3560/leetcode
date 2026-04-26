# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, [])]

        while stack:
            node, path = stack.pop()
            path = path + [node.val]

            total = 0
            for val in path[::-1]:
                total += val
                if total == targetSum:
                    count += 1

            if node.right:
                stack.append((node.right, path))
            if node.left:
                stack.append((node.left, path))

        return count

    def build_tree(vals):
        if not vals:
            return None

        root = TreeNode(vals[0])
        queue = [root]
        i = 1
        while i < len(vals):
            node = queue.pop(0)
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1

        return root

    
