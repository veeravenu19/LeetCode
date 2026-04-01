class Solution {
    public boolean isPowerOfTwo(int n) {
        int  i =0;
        while(true){
            if(n == Math.pow(2,i)){
                return true;
            }
            if(n < Math.pow(2,i)){
                return false;
            }
            i++;
        }
    }
}