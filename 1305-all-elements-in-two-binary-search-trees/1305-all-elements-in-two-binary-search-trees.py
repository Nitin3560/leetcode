# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(node: Optional[TreeNode], result: List[int]) -> None:
            if not node:
                return 
            
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)

        merged = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
            
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        
        return merged 
        