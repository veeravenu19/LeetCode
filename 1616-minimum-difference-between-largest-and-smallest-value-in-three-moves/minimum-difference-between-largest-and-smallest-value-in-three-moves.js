/**
 * @param {number[]} nums
 * @return {number}
 */
var minDifference = function(nums) {
    nums.sort((a,b)=>a-b);
    if(nums.length<=4){
        return 0;
    }
    else{
        var ans=nums[nums.length-1]-nums[0];
        // console.log(ans);
        for(var i=0;i<4;i++){
            ans=Math.min(ans,nums[nums.length-1-i]-nums[3-i]);
        }
        return ans;
    }

};