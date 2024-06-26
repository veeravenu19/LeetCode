class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        x=set(list(jewels))
        for i in stones:
            if i in x:
                c+=1
        return c