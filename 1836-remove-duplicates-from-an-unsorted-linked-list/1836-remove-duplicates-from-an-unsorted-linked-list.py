# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # dummy=ListNode(0)
        # dummy.next=head
        # node=dummy.next
        # while node:
        #     count=0
        #     next=dummy.next
        #     while next:
        #         if next.val==node.val:
        #             count+=1
        #         next=next.next
        #     if count>1:
        #         prev=dummy
        #         next=dummy.next
        #         while next:
        #             if next.val==node.val:
        #                 prev.next=next.next
        #             else:
        #                 prev=next
        #             next=next.next
        #         node=node.next
        #     else:
        #         node=node.next
        # return dummy.next
        dummy=ListNode(0)
        dummy.next=head
        freq={}
        node=dummy.next
        while node:
            if node.val in freq:
                freq[node.val]+=1
            else:
                freq[node.val]=1
            node=node.next
        prev=dummy
        curr=dummy.next
        while curr:
            if freq[curr.val]>1:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next