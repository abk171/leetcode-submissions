class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack();
        char c;
        for(int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if(c == ')') {
                if(!st.empty() && st.peek() == '(') st.pop();
                else return false;
            }
            else if(c == '}') {
                if(!st.empty() && st.peek() == '{') st.pop();
                else return false;
            }
            else if(c == ']') {
                if(!st.empty() && st.peek() == '[') st.pop();
                else return false;
            }
            else {
                st.push(c);
            }
            
        }
        if(st.empty()) return true;
        return false;
    }
}