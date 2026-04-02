class Solution {
    public int search(int[] nums, int target) {
        int ind = Arrays.binarySearch(nums,target);

        if(ind >= 0) {
            return ind;
        }
        else{
            return -1;
        }
    }
}