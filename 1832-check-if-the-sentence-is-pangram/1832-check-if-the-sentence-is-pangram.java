class Solution {
    public boolean checkIfPangram(String sentence) {
        int check = 0;
        for(int i = 0; i < sentence.length(); i++)
            check |= 1 << (sentence.charAt(i) - 'a');
        return check == (1 << 26) - 1;
    }
}