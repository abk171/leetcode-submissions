class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i : nums) {
            map.put(i, map.getOrDefault(i,0) + 1);
        }
        helper(result, new ArrayList<>(), map, nums.length);
        return result;
    }
    
    public void helper(List<List<Integer>> result, List<Integer> curr, HashMap<Integer, Integer> map, int size) {
        if(curr.size() == size) {
            result.add(new ArrayList<>(curr));
            return;
        }
        for(Integer key : map.keySet()) {
            
            
            if(map.get(key) == 0) continue;
            curr.add(key);
            map.put(key, map.get(key) - 1);
            helper(result, curr, map, size);
            curr.remove(curr.size() - 1);
            map.put(key, map.get(key) + 1);
            
            
            
            
        }
    }
    
}