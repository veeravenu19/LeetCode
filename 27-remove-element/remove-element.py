class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        while i<len(nums):
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)
        return nums.sort()