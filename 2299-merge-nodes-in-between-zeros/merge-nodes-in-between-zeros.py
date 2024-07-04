# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        z=0
        a=ListNode(0)
        b=a
        while head!=None:
            if head.val==0:
                z+=1
                head=head.next
            else:
                c+=head.val
                head=head.next
            if z==2:
                x=ListNode(c)
                c=0
                z=1
                b.next=x
                b=b.next
        return a.next

