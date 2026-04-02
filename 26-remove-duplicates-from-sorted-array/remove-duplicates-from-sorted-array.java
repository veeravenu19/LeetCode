class Solution {
    public int removeDuplicates(int[] nums) {
        int[] newArray = Arrays.copyOf(nums,nums.length);
        Arrays.fill(nums,-1);
        int c = 0;
        for(int i = 0; i<newArray.length;i++){
            if(Arrays.binarySearch(nums,0,c,newArray[i]) <0){
                nums[c] = newArray[i];
                c++;
            }
        }

        return c;   
    }
}