class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);

        int x = (int) nums.length/2;
        return nums[x];
    }
}