class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def isPalindrome(self,head):
        a=[]
        cur=head
        while cur:
            a.append(cur.val)
            cur=cur.next
        i=0
        j=len(a)-1
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True
