class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w)) 
        
        def dijkstra(src):
            heap = [(0, src)]
            distances = {src: 0}
            
            while heap:
                cost, node = heapq.heappop(heap)
                
                for neighbor, weight in graph[node]:
                    newcost = cost + weight
                    if neighbor not in distances or newcost < distances[neighbor]:
                        distances[neighbor] = newcost
                        heapq.heappush(heap, (newcost, neighbor))
            
            return distances
        
        result = -1
        mindist = float('inf')
        
        for city in range(n):
            distances = dijkstra(city)
            
            reachable = sum(1 for d in distances.values() if d <= distanceThreshold) - 1  
            
            if reachable <= mindist:
                mindist = reachable
                result = city
        
        return result