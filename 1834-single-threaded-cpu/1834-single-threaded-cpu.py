import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        result = []
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        def comEnq(task):
            return task[0]
        
        tasks.sort(key = comEnq)
        
        curTime = 0
        taskIndex = 0
        
        while taskIndex < len(tasks) or heap:
            if not heap and curTime < tasks[taskIndex][0]:
                curTime = tasks[taskIndex][0]
                
            while taskIndex < len(tasks) and curTime >= tasks[taskIndex][0]:
                _, processingTime, index = tasks[taskIndex]
                heapq.heappush(heap, (processingTime, index))
                taskIndex += 1
                
            processingTime, index = heapq.heappop(heap)
            
            curTime += processingTime
            result.append(index)
            
        return result
            
        
            
            
            
        
        