class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=set(nums)
        return ((3*sum(a))-sum(nums))//2