# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def getPath(root, target):
        #     if root is None:
        #         return None
        #     if root==target:
        #         return [root]
        #     left=getPath(root.left, target)
        #     if left:
        #         return [root]+left
        #     right=getPath(root.right, target)
        #     if right:
        #         return [root]+right
        #     return None
        # pathP=getPath(root, p)
        # pathQ=getPath(root, q)
        # lca=None
        # i=0
        # while i<len(pathP) and i<len(pathQ):
        #     if pathP[i]==pathQ[i]:
        #         lca=pathP[i]
        #     i+=1
        # return lca
        if root is None:
            return None
        if root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left, p, q)
        right=self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right