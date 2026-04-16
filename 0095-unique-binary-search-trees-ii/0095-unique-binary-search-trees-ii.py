# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end):
            if start > end:
                return [None]
            trees=[]
            for i in range(start, end + 1):
                for left in generate(start, i-1):
                    for right in generate(i+1, end):
                        node=TreeNode(i)
                        node.left=left
                        node.right=right
                        trees.append(node)
            return trees
        return generate(1, n)