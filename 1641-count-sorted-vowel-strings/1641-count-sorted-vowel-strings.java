class Solution {
    public int countVowelStrings(int n) {
        int[] store = new int[5];
        for(int i = 0; i < store.length; i++) store[i] = 1;
        while(n-- > 1) {
            for(int i = 3; i >= 0; i--) {
                store[i] += store[i+1];
            }
        }
        int result = 0;
        for(int i = 0; i < store.length; i++) result += store[i];
        return result;
    }
}