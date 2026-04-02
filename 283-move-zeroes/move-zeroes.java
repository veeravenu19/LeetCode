class Solution {
    public void moveZeroes(int[] nums) {
        int l = nums.length;
        int s = 0;
        int f = 0;

        while(f<l){
            if(nums[f] != 0){
                nums[s] = nums[f];
                s++;
            }
            f++;
        }

        for(int j = s;j<l;j++){
            nums[j] = 0;
        }
    }
}