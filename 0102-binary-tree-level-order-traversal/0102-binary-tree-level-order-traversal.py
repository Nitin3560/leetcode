# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # res=[]
        # q=deque([root])
        # while q:
        #     level=[]
        #     size=len(q)
        #     for _ in range(size):
        #         node=q.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(level)
        # return res
        def bfs(node, depth):
            if not node:
                return
            if depth==len(res):
                res.append([])
            res[depth].append(node.val)
            bfs(node.left, depth+1)
            bfs(node.right, depth+1)
        res=[]
        bfs(root, 0)
        return res