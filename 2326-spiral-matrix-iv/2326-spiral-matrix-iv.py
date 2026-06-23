# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for row in range(m)]
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        cur = head

        while cur and top <= bottom and left <= right:
            for c in range(left, right + 1):
                if not cur:
                    return ans
                ans[top][c] = cur.val
                cur = cur.next
            top += 1

            for r in range(top, bottom + 1):
                if not cur:
                    return ans
                ans[r][right] = cur.val
                cur = cur.next
            right -= 1

            for c in range(right, left - 1, -1):
                if not cur:
                    return ans
                ans[bottom][c] = cur.val
                cur = cur.next
            bottom -= 1

            for r in range(bottom, top - 1, -1):
                if not cur:
                    return ans
                ans[r][left] = cur.val
                cur = cur.next
            left += 1

        return ans