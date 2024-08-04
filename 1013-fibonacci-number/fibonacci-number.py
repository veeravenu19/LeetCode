class Solution:
    def fib(self, n: int) -> int:
        f=0
        s=1
        if(n==0):
            return 0 
        elif(n<=2):
            return 1
        else:
            while n-2!=0:
                temp=f
                f=s
                s=temp+s
                n-=1
            return f+s
