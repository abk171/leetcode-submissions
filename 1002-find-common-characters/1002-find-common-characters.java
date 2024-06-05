class Solution {
    public List<String> commonChars(String[] words) {
        int[] common = new int[26];
        int[] current = new int[26];
        
        for (char c: words[0].toCharArray()) {
            common[c - 'a']++;
        }
        for (int i = 1; i < words.length; i++) {
            for (char c: words[i].toCharArray()) {
                current[c - 'a']++;
            }
            for (int j = 0; j < 26; j++) {
                common[j] = common[j] < current[j] ? common[j] : current[j];
                current[j] = 0;
            }
        }
        List<String> result = new ArrayList();
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < common[i]; j++) {
                result.add(String.valueOf((char) (i + 'a')));
            }
        }
        return result;
    }
}