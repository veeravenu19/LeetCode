import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1=[]
        t = head
        while head !=None:
            n1.append(head.val)
            head = head.next
        if len(n1)==0:
            return head
        if k>len(n1):
            c = k%len(n1)
            for i in range(c):
                a = n1.pop()
                n1.insert(0,a)
        else:
            for i in range(k):
                a = n1.pop()
                n1.insert(0,a)
        b = ListNode(0)
        c=b
        for i in n1:
            b.next = ListNode(i)
            b = b.next
        return c.next