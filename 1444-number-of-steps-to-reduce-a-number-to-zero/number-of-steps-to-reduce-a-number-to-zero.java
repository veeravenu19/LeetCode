class Solution {
    public int numberOfSteps(int num) {
        int count = 0;
        
        if(num==0) return 0;
        while(true){
            count++;
            if(num%2 == 0){
                num = (int) num/2;
            }
            else{
                num-=1;
            }

            if(num==0){
                return count;
            }
        }
    }
}