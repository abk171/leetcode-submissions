class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        
        def euclid_distance(x1, y1, x2, y2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2
        
        for i in range(n):
            p1 = bombs[i]
            for j in range(i + 1, n):
                p2 = bombs[j]
                d = euclid_distance(p1[0], p1[1], p2[0], p2[1])
                
                if p1[2] ** 2 >= d: # p2 in p1s explosion radius
                    adj[i].append(j)
                if p2[2] ** 2 >= d:
                    adj[j].append(i)
        
        def dfs(node):
            st = []
            visited = [False for _ in range(n)]
            count = 0
            
            st.append(node)
            
            while st:
                x = st.pop()
                if visited[x]:
                    continue
                for y in adj[x]:
                    st.append(y)
                count = count + 1
                visited[x] = True
            
            return count
        
        maxbombs = 0
        for i in range(n):
            if dfs(i) > maxbombs:
                maxbombs = dfs(i)
        
        return maxbombs
        
            
                