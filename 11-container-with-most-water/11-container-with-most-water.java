class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int currentArea = 0;
        int start = 0;
        int end = height.length - 1;
        
        while(start < end) {
            currentArea = (end - start)*(Math.min(height[start], height[end]));
            maxArea = currentArea > maxArea ? currentArea : maxArea;
            if(height[start] < height[end]) start++;
            else end--;
        }
        
        return maxArea;
    }
}