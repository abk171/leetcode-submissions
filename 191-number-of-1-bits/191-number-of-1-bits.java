public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        if(n == 0) {
            return 0;
        }
        int count = 1;
        int b = 0;
        while(n!=1 && n!=0) {
            b = n&1;
            if(b==1) {
                count++;
            }
            n=n>>>1;
        }
        return count;
    }
}