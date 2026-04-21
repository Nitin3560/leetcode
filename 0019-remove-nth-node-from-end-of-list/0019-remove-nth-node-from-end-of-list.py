# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy=ListNode(0)
        # dummy.next=head
        # length=0
        # node=dummy.next
        # while node:
        #     length+=1
        #     node=node.next
        # target=length-n
        # prev=dummy
        # curr=dummy.next
        # for i in range(target):
        #     prev=curr
        #     curr=curr.next
        # prev.next=curr.next
        # return dummy.next
        dummy=ListNode(0, head)
        fast=slow=dummy
        for i in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next