class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        HashMap<Integer, Integer> cache = new HashMap();
        
        return dfs(cache, days, costs, 0);
        
    }
    
    public int dfs(HashMap<Integer, Integer> cache, int[] days, int[] costs, int i) {
        int n = days.length;
        int[] pass = new int[]{1, 7, 30};
        
        if (i >= n) {
            return 0;
        }
        else if (cache.containsKey(i)) {
            return cache.get(i);
        }
        else {
            cache.put(i, Integer.MAX_VALUE);
            for (int k = 0; k < 3; k++) {
                int j = i;
                while (j < n && days[j] < days[i] + pass[k]) {
                    j += 1;
                }
                cache.put(i, Math.min(cache.get(i), costs[k] + dfs(cache, days, costs, j)));
            }
        }
        
        return cache.get(i);

    }
}