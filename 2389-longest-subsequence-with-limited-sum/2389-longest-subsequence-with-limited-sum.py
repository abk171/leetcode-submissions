class Solution(object):
    def prefixSum(self, nums):
        result = [0 for _ in range(len(nums))]
        s = 0
        for i, num in enumerate(nums):
            s = s + num
            result[i] = s
        
        return result
    
    def binarySearch(self, search, prefix):
              
        start = 0
        end = len(prefix) - 1
        
        
        while(start < end):
            mid = (start + end) // 2
            if prefix[mid] == search:
                return mid + 1
            elif prefix[mid] > search:
                end = mid - 1
            else:
                start = mid + 1
        return start if prefix[start] > search else start + 1
                
            
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        prefix = self.prefixSum(nums)
        
        result = []
        for i in queries:
            result.append(self.binarySearch(i, prefix))
            
        return result
        