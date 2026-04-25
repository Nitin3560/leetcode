class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        visited[source] = True
        queue = [source]
        head = 0 

        while head < len(queue):
            node = queue[head]
            head += 1
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False