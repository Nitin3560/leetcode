# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        values=[]
        node=dummy.next
        while node:
            values.append(node.val)
            node=node.next
        less=[]
        greater=[]
        for val in values:
            if val<x:
                less.append(val)
            else:
                greater.append(val)
        result=less+greater
        node=dummy.next
        for val in result:
            node.val=val
            node=node.next
        return dummy.next
