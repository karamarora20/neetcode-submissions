# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # lim=n
        # if n==1 and head.next==None:
        #     return None
        prev=None
        curr=head
        while(curr.next):
            if n<=1:
                prev=prev.next if prev else head
            n-=1
            curr=curr.next
        if prev and prev.next:
            prev.next=prev.next.next
        else:
            head=head.next
        
        return head