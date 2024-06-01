class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        int i = 0;
        int j = n - 1;
        
        while (j >= 0 && i >= 0 
               && j < n && i < m) {
            if (matrix[i][j] == target) {
                return true;
            }
            else if (matrix[i][j] < target) {
                i += 1;
            }
            else {
                j -= 1;
            }
        }
        return false;
    }
}