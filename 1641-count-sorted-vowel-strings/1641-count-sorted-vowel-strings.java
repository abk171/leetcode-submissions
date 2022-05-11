class Solution {
    public int countVowelStrings(int n) {
        char[] arr = {'a', 'e', 'i', 'o', 'u'};
        List<String> result = new ArrayList<>();
        helper(result, new StringBuilder(), n, 0, arr);
        // System.out.println(result.toString());
        return result.size();
    }
    
    public void helper(List<String> result, StringBuilder curr, int n, int index, char[] arr) {
        if(n <= 0) {
            result.add(curr.toString());
            return;
        }
        for(; index < arr.length; index++) {
            curr.append(arr[index]);
            helper(result,curr,n-1,index, arr);
            curr.deleteCharAt(curr.length() - 1);
        }
    }
}