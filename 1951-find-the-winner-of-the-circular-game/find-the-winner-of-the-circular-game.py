class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[i for i in range(1,n+1)]
        c=0
        z=0
        f=1
        while len(l)!=1:
            for i in range(len(l)):
                if l[i]!=0:
                    c+=1
                if c==k:
                    c=0
                    l[i]=0
                    z+=1
                if z==len(l)-1:
                    f=0
                    break
            if f==0:
                break
        for i in l:
            if i!=0:
                return i
        # print(l)
        return 0