class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList();
        if(digits.length() == 0) return result;
        char[][] map = {
            {'a','b','c'},
            {'d','e','f'},
            {'g','h','i'},
            {'j','k','l'},
            {'m','n','o'},
            {'p','q','r','s'},
            {'t','u','v'},
            {'w','x','y','z'}
        };
        
        // List<String> result = new ArrayList<>();
        StringBuilder curr = new StringBuilder();
        helper(result, map, digits, 0, curr);
        return result;       
    }
    
    public void helper(List<String> result, char[][] map, String digits, int i, StringBuilder curr) {
        if(i >= digits.length()) {
            result.add(curr.toString());
            // curr.deleteCharAt(curr.length() - 1);
            return;
        }
        for(char c : map[digits.charAt(i++) - '2']) {
            helper(result, map, digits, i, curr.append(c));
            curr.deleteCharAt(curr.length() - 1);
        }
    }
}