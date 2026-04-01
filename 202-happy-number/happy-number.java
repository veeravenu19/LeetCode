class Solution {
    public static int addSquare(int n){
        int c = 0;
        while(n!=0){
            int temp = n%10;
            c = c+(temp*temp);
            n = (int) n/10;
        }

        return c;

    }

    public boolean isHappy(int n) {
        boolean[] seen = new boolean[1000];
        Arrays.fill(seen,false);
        while(true){
            if(addSquare(n) == 1){
                return true;
            }
            n=addSquare(n);
            if(seen[n]){
                return false;
            }
            seen[n] = true;
        }
    }
}