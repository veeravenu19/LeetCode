class Solution {
    public int fib(int n) {
        int f=0,s=1;
        if(n==0) return 0;
        if(n<=2) return 1;
        else{
            while(n-3 >= 0){
                int temp = f;
                f=s;
                s=temp+s;
                n--;
            }
            return f+s;
        }
    }
}