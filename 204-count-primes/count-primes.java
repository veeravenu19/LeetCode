class Solution {
    public static boolean isPrime(int n){
        if(n<=1){
            return false;
        }
        for(int i = 2 ; i*i<=n;i++){
            if(n%i == 0){
                return false;
            }
        }
        return true;
    }
    public int countPrimes(int n) {
        if(n<=2) return 0;
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;


        for (int p = 2; p * p < n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i < n; i += p)
                    isPrime[i] = false;
            }
        }

        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) count++;
        }

        return count;
    }
}