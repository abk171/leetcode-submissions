class Solution {
    public boolean hasAllCodes(String s, int k) {
        if(s.length() < (int)Math.pow(2,k)) return false;
        StringBuilder sb = new StringBuilder();
        HashSet<String> set = new HashSet<>();
        
        for(int i = 0; i < k; i++) {
            sb.append(s.charAt(i));
        }
        
        set.add(sb.toString());
        
        for(int i = k; i < s.length(); i++) {
            sb.append(s.charAt(i));
            sb.deleteCharAt(0);
            set.add(sb.toString());
        }
        // System.out.println(set.toString());
        if(set.size() == (int)Math.pow(2,k)) return true;
        return false;
    }
}