# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def dfs(node):
            if not node:
                return 1
            carry = dfs(node.next) 
            s = node.val + carry
            node.val = s % 10
            return s // 10 

        carry = dfs(head)
        if carry: 
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        return head