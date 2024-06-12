class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        remaining = []
        result = []
        
        for e in arr2:
            count[e] = 0
        
        for e in arr1:
            if e in count:
                count[e] += 1
            else:
                remaining.append(e)
        
        remaining.sort()
        
        for e in arr2:
            for i in range(count[e]):
                result.append(e)
        
        result += remaining
        
        return result