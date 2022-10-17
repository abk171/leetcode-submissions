class Solution {
    public boolean checkIfPangram(String sentence) {
        int check = 0;
        for(char c: sentence.toCharArray())
            check |= 1 << (c - 'a');
        return check == (1 << 26) - 1;
    }
}