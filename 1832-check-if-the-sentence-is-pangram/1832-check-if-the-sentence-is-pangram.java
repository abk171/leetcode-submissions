class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] found = new boolean[26];
        for(char c : sentence.toCharArray())
            found[c - 97] = true;
        int count = 0;
        for(boolean b : found)
            if(b == true) count++;
        
        if(count == 26) return true;
        return false;
    }
}