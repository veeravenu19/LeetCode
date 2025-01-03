from typing import List  

class Solution:  
    def waysToSplitArray(self, nums: List[int]) -> int:  
        n = len(nums)  
        total_sum = sum(nums)  
        left_sum = 0  
        valid_splits = 0  
        
        # We loop until n-1 because we can't split after the last element  
        for i in range(n - 1):  
            left_sum += nums[i]  
            right_sum = total_sum - left_sum  
            
            # Check if left_sum is greater than or equal to right_sum  
            if left_sum >= right_sum:  
                valid_splits += 1  
        
        return valid_splits