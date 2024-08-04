def fun(nums,i,j,t):
    if i>j:
        return -1
    else:
        mid=(i+j)//2
        if nums[mid]==t:
            return mid
        elif nums[mid]<t:
            return fun(nums,mid+1,j,t)
        else:
            return fun(nums,i,mid-1,t)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        nums.sort()
        return fun(nums,i,j,target)