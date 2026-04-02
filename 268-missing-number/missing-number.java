class Solution {
    public int missingNumber(int[] nums) {
        int l = nums.length;
        int Total_sum = (l*(l+1))/2;
        int sum = 0;

        for(int i=0;i<l;i++){
            sum += nums[i];
        }
        
        return Total_sum-sum;
    }

}