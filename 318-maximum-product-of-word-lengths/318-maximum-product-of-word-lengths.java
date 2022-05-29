class Solution {
    
    
    public int maxProduct(String[] words) {
        Arrays.sort(words, new Comparator<String>() {
           @Override
            public int compare(String a, String b) {
                return Integer.compare(a.length(), b.length()) * -1;
            }
        });
        int[] masks = new int[words.length];
        for(int i = 0; i < words.length; i++)
            for(int j = 0; j < words[i].length(); j++)
                masks[i] |= 1 << (words[i].charAt(j) - 'a');
        int max = 0;
        int b_and = 0;
        int product = 0;
        for(int i = 0; i < words.length; i++) {
            for(int j = i + 1; j < words.length; j++) {
                b_and = masks[i] & masks[j];
                if(b_and == 0) {
                    product = words[i].length() * words[j].length();
                    max = max > product ? max : product;
                }
            }
        }
        return max;
       
    }
}