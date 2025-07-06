# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d= {}
        while head !=None:
            if head.val not in d:
                d[head.val] = 1
                head = head.next
            else:
                d[head.val]+=1
                head = head.next
        n = ListNode(0)
        a=n
        for k,v in d.items():
            if v==1:
                n.next = ListNode(k)
                n = n.next
            else:
                continue
        return a.next
