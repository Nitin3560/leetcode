# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove = set(nums)
        dummy = ListNode(0, head)
        prev, cur = dummy, head
    
        while cur:
            if cur.val in remove:
                prev.next = cur.next 
            else:
                prev = cur
            cur = cur.next
    
        return dummy.next