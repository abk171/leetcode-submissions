class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, new Comparator<int[]>() {
           public int compare(int[] a, int[] b) {
               return a[1] - b[1];
           } 
        });
        
        int count = 1;
        int max = points[0][1];
        
        for(int i = 1; i < points.length; i++) {
            if(max >= points[i][0] && max <= points[i][1]) continue;
            else {
                count++;
                max = points[i][1];
            }
        }  
        return count;
    }
}