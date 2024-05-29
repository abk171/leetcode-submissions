class Solution {
    public int numSteps(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
        }
        
        int steps = 0;
        
        while(sb.length() > 1) {
            if (sb.charAt(0) == '0') {
                sb.deleteCharAt(0);
            }
            else {
                int j = 0;
                while(j < sb.length() && sb.charAt(j) == '1') {
                    sb.setCharAt(j, '0');
                    j += 1;
                }
                if (j == sb.length()) {
                    sb.append('1');
                }
                else {
                    sb.setCharAt(j, '1');
                }
            }
            
            steps += 1;
        }
        
        return steps;
    }
}