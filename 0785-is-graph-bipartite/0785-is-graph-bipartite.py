class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        group = {}
        queue = []
        curr = 0

        for start in range(n):
            if start in group:
                continue

            queue.append(start)
            group[start] = 0

            while curr < len(queue):
                node = queue[curr]
                curr += 1

                for neighbor in graph[node]:
                    if neighbor not in group:
                        group[neighbor] = 1 - group[node]
                        queue.append(neighbor)
                    elif group[neighbor] == group[node]:
                        return False

        return True