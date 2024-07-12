class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def fun(s,sub,v):
            l=[]
            c=0
            for i in s:
                l.append(i)
                if len(l)!=0 and ''.join(l[-2:])==sub:
                    l.pop()
                    l.pop()
                    c+=v
            return c,"".join(l)
        if y<x:
            sub1="ab"
            v1=x
            sub2="ba"
            v2=y
        else:
            sub1="ba"
            v1=y
            sub2="ab"
            v2=x
        c1,r=fun(s,sub1,v1)
        c2,r=fun(r,sub2,v2)
        return c1+c2