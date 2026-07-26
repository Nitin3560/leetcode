class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = []
        for i in range(n):
            graph.append([])
        
        for conn in connections:
            a = conn[0]
            b = conn[1]
            graph[a].append([b, 1])  
            graph[b].append([a, 0])  
        
        visited = []
        for i in range(n):
            visited.append(False)
        
        visited[0] = True
        
        queue = [0]
        front = 0
        count = 0
        
        while front < len(queue):
            node = queue[front]
            front += 1
            
            neighbors = graph[node]
            for i in range(len(neighbors)):
                neighbor = neighbors[i][0]
                cost = neighbors[i][1]
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += cost
                    queue.append(neighbor)
        
        return count