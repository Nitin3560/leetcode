# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head or m == 0:
            return None
        if n == 0:
            return head

        curr = head
        while curr:
            for _ in range(1, m):       
                if not curr:
                    break
                curr = curr.next
            if not curr:
                break

            to_delete = curr.next
            for _ in range(n):
                if not to_delete:
                    break
                to_delete = to_delete.next

            curr.next = to_delete
            curr = to_delete

        return head