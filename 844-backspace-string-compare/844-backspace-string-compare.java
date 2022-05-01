class Solution {
    public boolean backspaceCompare(String s, String t) {
        int skip = 0;
        int i = s.length() - 1;
        
        StringBuilder s1 = new StringBuilder();
        StringBuilder s2 = new StringBuilder();
        
        char c;
        
        while(i >= 0) {
            c = s.charAt(i);
            
            if(c == '#') skip++;
            else {
                if(skip > 0) skip--;
                else s1.append(c);
            }
            i--;
        }
        
        i = t.length() - 1;
        skip = 0;
        
        while(i >= 0) {
            c = t.charAt(i);
            
            if(c == '#') skip++;
            else {
                if(skip > 0) skip--;
                else s2.append(c);
            }
            i--;
        }
        
        if(s1.toString().compareTo(s2.toString()) == 0) return true;
        return false;
        
    }
}