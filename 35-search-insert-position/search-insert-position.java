class Solution {
    public int searchInsert(int[] nums, int target) {

        int ind = Arrays.binarySearch(nums,target); 
        if(ind >=0){
            return ind;
        }
        else{
            return (-1)*(ind+1);
        }
        
    }
}