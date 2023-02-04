class Solution {
    
    public class store {
        int length;
        int[] frequency;
        
        public store() {
            length = 0;
            frequency = new int[26];
        }
        
        public void increment(int index) {
            frequency[index]++;
            length++;
        }
        
        public void decrement(int index) {
            frequency[index]--;
            length--;
        }
        
        public boolean compare(store other) {
            if(this.length == other.length) {
                for(int i = 0; i < 26; i++) {
                    if(this.frequency[i] != other.frequency[i])
                        return false;
                }
                return true;
            }
            return false;
        }
        
        public void create(String s) {
            for(int i = 0; i < s.length(); i++)
                increment(s.charAt(i) - 'a');
        }
    }
    
    public boolean checkInclusion(String s1, String s2) {
        
        if(s1.length() > s2.length()) return false;
        
        store window = new store();
        store sample = new store();
        sample.create(s1);
        
        for(int i = 0; i < s1.length(); i++)
            window.increment(s2.charAt(i) - 'a');
        
        if(window.compare(sample)) return true;
        
        int start = 1;
        int end = s1.length();
        
        for(int i = 0; i < s2.length() - s1.length(); i++) {
            window.increment(s2.charAt(end) - 'a');
            window.decrement(s2.charAt(start - 1) - 'a');
            if(window.compare(sample)) return true;
            start++;
            end++;
        }
        
        return false;
    }
}