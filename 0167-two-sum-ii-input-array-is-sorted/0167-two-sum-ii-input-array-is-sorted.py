class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(arr, val):
            low = 0
            high = len(arr) - 1
            
            while low < high:
                mid = (low + high) // 2
                if arr[mid] == val:
                    return mid
                elif arr[mid] > val:
                    high = mid - 1
                else:
                    low = mid + 1
                
            return low
        
        left, right = 0, len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right]
            
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        
        

         