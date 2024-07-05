# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l=[]
        temp = head.next
        prev = head
        ind = 1
        while temp.next is not None:
            if temp.val > temp.next.val and temp.val > prev.val:
                l.append(ind)
            elif temp.val < temp.next.val and temp.val < prev.val:
                l.append(ind)
            ind += 1
            prev = temp
            temp = temp.next
        i=0
        j=1
        a=len(l)-1
        l1=[]
        print(a)
        print(l)
        while a>0:
            print(l[j]-l[i])
            l1.append(l[j]-l[i])
            i+=1
            j+=1
            a-=1
        print(l1)
        if len(l1)<1:
            return [-1,-1]
        return [min(l1),l[-1]-l[0]]