class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]  
        distances = {}
        
        while heap:
            cost, node = heapq.heappop(heap)
            
            if node in distances:
                continue    

            distances[node] = cost
            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(heap, (cost + weight, neighbor))
        
        if len(distances) == n:
            return max(distances.values())
            
        return -1