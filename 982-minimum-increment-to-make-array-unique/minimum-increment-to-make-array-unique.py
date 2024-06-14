class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                a=nums[i-1]+1
                c+=a-nums[i]
                nums[i]=a
        return c
       