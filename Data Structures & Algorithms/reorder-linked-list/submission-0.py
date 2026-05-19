# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        new_h=ListNode()
        p1,p2=head,head
        while(p2 and p2.next):
            p1=p1.next
            p2=p2.next.next
        mid=p1.next
        p1.next=None
        end=None
        while(mid):
            temp=mid.next
            mid.next=end
            end=mid
            mid=temp
        st=head
        while(end):
            tmp1=st.next
            tmp2=end.next
            st.next=end
            end.next=tmp1
            end=tmp2
            st=tmp1
        
        

        