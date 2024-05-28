class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        return bfs(maze, entrance);
    }
    
    public int bfs(char[][] maze, int[] cell) {
        int m = maze.length;
        int n = maze[0].length;
        
        int[] start = new int[]{cell[0], cell[1], 0};
        
        int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        Queue<int[]> q = new LinkedList();
        q.add(start);
        
        while(q.size() > 0) {
            int[] current = q.remove();
            
            if (current[0] >= 0 && current[0] < m
               && current[1] >= 0 && current[1] < n
               && maze[current[0]][current[1]] == '.') {
                maze[current[0]][current[1]] = '+';
                
                if (current[0] == 0 || current[0] == m - 1 || current[1] == 0 || current[1] == n - 1) {
                    if(current[0] != cell[0] || current[1] != cell[1]) {
                        return current[2];
                    }
                }
                
                for (int i = 0; i < 4; i++) {
                    int[] next = new int[]{current[0] + direction[i][0],
                                          current[1] + direction[i][1],
                                          current[2] + 1};
                    q.add(next);
                }
            }
        }
        
        return -1;
    }
}