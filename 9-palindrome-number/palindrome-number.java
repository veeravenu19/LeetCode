class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);

        StringBuffer sb = new StringBuffer(s);
        sb.reverse();

        String reve = sb.toString();

        return reve.equals(s);
    }
}