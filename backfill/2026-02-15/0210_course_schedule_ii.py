from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
