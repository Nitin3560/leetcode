# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesshead= ListNode(0)
        greaterhead= ListNode(0)
        less= lesshead
        greater= greaterhead
        curr= head
        while curr:
            if curr.val < x:
                less.next= curr
                less =less.next
            else:
                greater.next =curr
                greater =greater.next
            curr =curr.next
        greater.next =None
        less.next =greaterhead.next
        return lesshead.next