class Solution {

    public static int ad(int a){
        int s = 0;
        while(a!=0){
            int temp = a%10;
            s += temp;
            a = (int) a/10;
        }

        return s;
    }
    public int addDigits(int num) {
        while(true){
            if(ad(num) < 10){
                return ad(num);
            }
            num = ad(num);
        }
    }
}