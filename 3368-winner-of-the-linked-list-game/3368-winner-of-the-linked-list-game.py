# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even_score = 0
        odd_score = 0
        i = 0
        curr = head
    
        while curr and curr.next:
            even_val = curr.val
            odd_val = curr.next.val
        
            if even_val > odd_val:
                even_score += 1
            elif odd_val > even_val:
                odd_score += 1
        
            curr = curr.next.next  
        if even_score > odd_score:
            return "Even"
        elif odd_score > even_score:
            return "Odd"
        else:
            return "Tie"