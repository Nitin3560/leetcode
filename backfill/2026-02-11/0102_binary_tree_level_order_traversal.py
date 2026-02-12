from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            size = len(q)
            lvl = []
            for _ in range(size):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lvl)
        return res
