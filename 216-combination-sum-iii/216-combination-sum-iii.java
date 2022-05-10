class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        ArrayList<List<Integer>> res = new ArrayList<>();
        helper(1, k, n, new ArrayList<>(), res);
        return res;
    }
    public void helper(int start, int k, int n, List<Integer> temp, List<List<Integer>> res){
        if(n < 0) return;
        if(n == 0 && temp.size() == k){
            res.add(new ArrayList<>(temp));
            return;
        }
        for(;start < 10; start++){
            temp.add(start);
            helper(start + 1, k, n -start, temp, res);
            temp.remove(temp.size() - 1);
        }
    }
}