class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        
        String[] words = sentence.split(" ");
        for(int i = 0; i < words.length; i++) {
            if(words[i].length() < searchWord.length()) continue;
            else if(checkPrefix(words[i], searchWord)) return i+1;
        }
        return -1;
    }
    
    public boolean checkPrefix(String a, String b) {
        int i = 0;
        int j = 0;
        
        while(i < a.length() && j < b.length()) {
            if(a.charAt(i) != b.charAt(j)) return false;
            i++;
            j++;
        }
        return true;
    }
}