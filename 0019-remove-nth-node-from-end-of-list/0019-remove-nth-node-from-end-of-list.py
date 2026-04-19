# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        length=0
        node=dummy.next
        while node:
            length+=1
            node=node.next
        target=length-n
        prev=dummy
        curr=dummy.next
        for i in range(target):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        return dummy.next
    