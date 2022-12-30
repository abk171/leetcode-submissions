class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []
        self.backtrack(0, graph, [0], results)
        return results
        
    def backtrack(self, current, graph, result, results):
        
        
        if current == len(graph) - 1:
            results.append(list(result))
            return 
        
        for x in graph[current]:
            result.append(x)
            self.backtrack(x, graph, result, results)
            result.pop()
            
            
    
    