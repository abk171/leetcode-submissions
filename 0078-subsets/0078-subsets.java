class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList();
        List<Integer> subset = new ArrayList();
        
        backtrack(nums, subset, result, 0);
        
        return result;
        
    }
    
    public void backtrack(int[] nums, List<Integer> subset, List<List<Integer>> result, int i) {
        int n = nums.length;
        if (i >= n) {
            result.add(new ArrayList(subset));
            return;
        }
        
        subset.add(nums[i]);
        backtrack(nums, subset, result, i + 1);
        subset.remove(subset.size() - 1);
        backtrack(nums, subset, result, i + 1);
        
    }
}