# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        ans=ListNode()
        new_h=ans
        n1,n2=l1,l2
        while(n1 and n2):
            s=n1.val+n2.val+carry
            curr_ans_dig=(s)%10
            carry= s//10
            new_h.next=ListNode(curr_ans_dig)
            new_h=new_h.next
            n1=n1.next
            n2=n2.next
        while n1:
            s=n1.val+carry
            curr_ans_dig=(s)%10
            carry= s//10
            new_h.next=ListNode(curr_ans_dig)
            new_h=new_h.next
            n1=n1.next
            
        while n2:
            s=n2.val+carry
            curr_ans_dig=(s)%10
            carry= s//10
            new_h.next=ListNode(curr_ans_dig)
            new_h=new_h.next
            n2=n2.next
        if carry>0:
            new_h.next=ListNode(carry)
        return ans.next


