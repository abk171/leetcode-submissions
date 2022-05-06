class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<int[]> st = new Stack();
        char c;
        for(int i = 0; i < s.length(); i++) {
            
            c = s.charAt(i);
            
            if(st.empty() || st.peek()[0] != c) {
                st.push(new int[] {c, 1});
            }
            else {
                st.peek()[1]++;
            }
            
            if(st.peek()[1] == k) st.pop();
        }
        StringBuilder result = new StringBuilder();
        for(int[] a : st) {
            while(a[1]-- > 0) result.append((char)a[0]);
        }
        
        return result.toString();
    }
}