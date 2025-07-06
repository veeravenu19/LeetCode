# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        # if l1.val == 0:
        #     return l2
        # if l2.val == 0:
        #     return l1
        while l1!=None:
            
            n1 +=str(l1.val)
            l1=l1.next
        while l2!=None:
            n2 += str(l2.val)
            l2 = l2.next
        # print(n1[::-1])
        # print(n2)
        s = int(n1[::-1])+int(n2[::-1]) 
        n = ListNode(0)
        if s==0:
            return n
        # # print(s)
        a=n
        while s!=0:
            t = s%10
            a.next = ListNode(t)
            a = a.next
            s = s//10
        return n.next