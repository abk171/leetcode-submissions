class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int evenPtr = 0;
        int oddPtr = nums.length - 1;
        int[] result = new int[nums.length];
        
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] % 2 == 0) result[evenPtr++] = nums[i];
            else result[oddPtr--] = nums[i];
        }
        
        return result;
    }
}