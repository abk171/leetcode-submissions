class Solution {
    int count = 0;
    public int countVowelStrings(int n) {
        
        // char[] arr = {'a', 'e', 'i', 'o', 'u'};
        helper(n, 0);
        return count;
    }
    
    public void helper(int n, int index) {
        // System.out.println(count);
        if(n <= 0) {
            count++; return;
        }
        
        for(;index < 5; index++) {
            helper( n - 1, index);
        }
    }
}