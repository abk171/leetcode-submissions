class Solution:
    ## elect the boss
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0] #3
        cnt = 0 #0
        
        for i in nums: #3 2
            if i != ele:
                cnt -= 1 # 0
                if cnt == 0:
                    ele = i #2
                    cnt = 1 
                    print(ele, i)
            else:
                cnt += 1 #1
        
        return ele
                
        
        
# class Solution {
# public:
#     int majorityElement(vector<int>& nums) {
#         int ele = nums[0], cnt = 0;

#         for(auto it: nums){
#             if(it != ele){
#                 cnt--;
#                 if(cnt == 0){
#                     ele = it;
#                     cnt = 1;
#                 }
#             }
#             else cnt++;
#         }
#         return ele;
#     }
# };