# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy

        while True:
            end = before
            count = 0

            while end and count < k:
                end = end.next
                count += 1

            if not end:
                break 

            after = end.next
            start = before.next

            prev = after
            curr = start

            while curr != after:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node

            before.next = end
            before = start

        return dummy.next