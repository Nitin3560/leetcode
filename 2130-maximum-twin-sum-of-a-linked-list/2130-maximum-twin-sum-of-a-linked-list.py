# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        maxsum = 0
        first = head
        second = prev
        while second is not None:
            maxsum = max(maxsum, first.val + second.val)
            first = first.next
            second = second.next

        return maxsum
