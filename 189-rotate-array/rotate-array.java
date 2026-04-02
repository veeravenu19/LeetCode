class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        // if(k > nums.length) return;

        int[] SecondArray = Arrays.copyOfRange(nums,nums.length-k,nums.length);
        int[] FirstArray = Arrays.copyOfRange(nums,0,nums.length-k);

        for(int i = 0;i<SecondArray.length;i++){
            nums[i] = SecondArray[i];
        }

        for(int i = 0 ;i<FirstArray.length;i++){
            nums[k+i] = FirstArray[i];
        }

    }
}