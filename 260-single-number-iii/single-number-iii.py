class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for k,v in d.items():
            if v==1:
                l.append(k)
        return l