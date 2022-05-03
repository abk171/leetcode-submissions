class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int start = -1;
        int end = -1;
        
        int prev = 0;
    
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] < nums[prev]) end = i;
            else prev = i;
        }
        
        prev = nums.length - 1;
        
        for(int i = nums.length - 1; i >= 0; i--) {
            if(nums[i] > nums[prev]) start = i;
            else prev = i;
        }
        
        return (start >= 0 && end >= 0) ? (end - start) + 1 : 0;
    }
}