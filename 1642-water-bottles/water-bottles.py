class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        c=b
        while True:
            if b<e:
                break
            if b%e==0:
                c+=b//e
                b=b//e
            else:
                c+=b//e
                b=b//e+b%e
        return c