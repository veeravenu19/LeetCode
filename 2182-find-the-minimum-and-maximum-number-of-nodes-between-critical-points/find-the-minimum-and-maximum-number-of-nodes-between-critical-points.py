# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l=[]
        copy=head.next
        pre=head.val
        i=0
        while copy.next!=None:
            if copy.val>copy.next.val and copy.val>pre:
                l.append(i)
            elif copy.val<copy.next.val and copy.val<pre:
                l.append(i)
            i+=1
            pre=copy.val
            copy=copy.next
        i=0
        j=1
        a=len(l)-1
        l1=[]
        # print(a)
        # print(l)
        while a>0:
            # print(l[j]-l[i])
            l1.append(l[j]-l[i])
            i+=1
            j+=1
            a-=1
        print(l1)
        if len(l1)<1:
            return [-1,-1]
        return [min(l1),l[-1]-l[0]]