class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        for node in range(n):
            if node not in visited:
                stack = [node]
                while stack:
                    curr = stack.pop()   
                    if curr in visited:
                        continue
                    visited.add(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                components += 1

        return components