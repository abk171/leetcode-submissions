class Solution {
    public boolean find132pattern(int[] nums) {
        if(nums.length < 3) return false;
        Stack<int[] > st = new Stack();
        int min = nums[0];
        for(int i = 1; i < nums.length; i++) {
            while(!st.empty() && nums[i] >= st.peek()[0]) st.pop();
            if(!st.empty() && nums[i] > st.peek()[1]) return true;
            st.push(new int[] {nums[i], min});
            min = min < nums[i] ? min : nums[i];
        }
        return false;
        
    }
}