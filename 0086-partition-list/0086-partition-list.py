# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        ge_dummy = ListNode(0)
        less_tail, ge_tail = less_dummy, ge_dummy

        curr = head
        while curr:
            nxt = curr.next 
            curr.next = None
            if curr.val < x:
                less_tail.next = curr
                less_tail = less_tail.next
            else:
                ge_tail.next = curr
                ge_tail = ge_tail.next
            curr = nxt

        less_tail.next = ge_dummy.next
        return less_dummy.next