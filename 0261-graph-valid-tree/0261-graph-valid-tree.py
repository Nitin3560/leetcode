class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = []
        for i in range(n):
            graph.append([])
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        
        stack = [(0, -1)]  
        
        while stack:
            node, parent = stack.pop()
            
            if visited[node]:
                return False 
            
            visited[node] = True
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))
        
        for i in range(n):
            if not visited[i]:
                return False
        
        return True