class Solution {
    public static int addition(int n ){
        int c= 0;
        while(n!=0){
            int temp = n%10;
            c+=temp;
            n = (int) n/10;
        }

        return c;
    }

    public int sumOfTheDigitsOfHarshadNumber(int x) {
        if(x%addition(x) ==0){
            return addition(x);
        }
        else{
            return -1;
        }
    }
}