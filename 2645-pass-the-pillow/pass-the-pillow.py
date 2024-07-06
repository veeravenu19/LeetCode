class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p=1
        path=True
        for i in range(1,time+1):
            if path:
                p+=1
                if p>n:
                    p=n-1
                    path=False
            else:
                p-=1
                if p<1:
                    p=2
                    path=True
        return p