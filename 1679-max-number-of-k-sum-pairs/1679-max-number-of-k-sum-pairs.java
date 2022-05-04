class Solution {
    public int maxOperations(int nums[], int k) {
        int count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        HashSet<Integer> visited = new HashSet<>();
        
        for(int i = 0; i < nums.length; i++) {
            if(map.containsKey(nums[i])) map.put(nums[i], map.get(nums[i]) + 1);
            else map.put(nums[i], 1);
        }
        
        // for(Integer key : map.keySet()) {
        //     System.out.printf("%d : %d\n", key, map.get(key));
        // }
        
        for(Integer key : map.keySet()) {
            if(visited.contains(key)) continue;
            else {
                if(k % 2 == 0 && key == k/2) count += map.get(key)/2;
                else if(map.containsKey(k - key)) count += Math.min(map.get(key), map.get(k - key));
                visited.add(k - key);
            }
        }
        
        return count;
    }
}