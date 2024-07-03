class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=4:
            return 0
        else:
            ans=nums[len(nums)-1]-nums[0]
            for i in range(0,4):
                ans=min(ans,nums[len(nums)-1-i]-nums[3-i])
            return ans