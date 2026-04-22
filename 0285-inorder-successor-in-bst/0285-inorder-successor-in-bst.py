# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # inorder=[]
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     inorder.append(node)
        #     dfs(node.right)
        # dfs(root)
        # for i in range(len(inorder)-1):
        #     if inorder[i].val==p.val:
        #         return inorder[i+1]
        # return None
        def dfs(node, found, successor):
            if not node or successor:
                return found, successor
            found, successor=dfs(node.left, found, successor)
            if successor:
                return found, successor
            if found and not successor:
                successor=node
                return found, successor
            if node.val==p.val:
                found=True
            found, successor=dfs(node.right, found, successor)
            return found, successor
        _, successor=dfs(root, False, None)
        return successor