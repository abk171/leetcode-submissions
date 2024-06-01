class Solution {
    public int scoreOfString(String s) {
        int sum = 0;
        for(int i = 1; i < s.length(); i++) {
            sum += (s.charAt(i) > s.charAt(i - 1)) ? s.charAt(i) - s.charAt(i - 1) : s.charAt(i - 1) - s.charAt(i);
        }
        return sum;
    }
}