class Solution {
    public class Pair {
        char c;
        int n;
        
        public Pair(char curr) {
            c = curr;
            n = 1;
        }
        
        public void increment() {
            n++;
        }
        
        public String stringRep() {
            StringBuilder s = new StringBuilder();
            for(int i = 0; i < n; i++) s.append(c);
            return s.toString();
        }
    }
    public String removeDuplicates(String s, int k) {
        Stack<Pair> st = new Stack();
        char curr;
        for(int i = 0; i < s.length(); i++) {
            
            curr = s.charAt(i);
            if(st.empty() || st.peek().c != curr) st.push(new Pair(curr));
            else st.peek().increment();
            
            
            if(st.peek().n == k) st.pop();
        }
        
        StringBuilder result = new StringBuilder();
        while(!st.empty()) {
            result.append(st.pop().stringRep());
        }
        return result.reverse().toString();
    }
}