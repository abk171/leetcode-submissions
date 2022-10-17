class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] found = new boolean[26];
        for(char c : sentence.toCharArray())
            found[c - 97] = true;
        for(boolean f: found)
            if(!f) return false;
        return true;
    }
}