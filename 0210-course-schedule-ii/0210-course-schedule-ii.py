class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[pre].append(course)

        indegree = [0] * numCourses
        for course, pre in prerequisites:
            indegree[course] += 1

        queue = deque(node for node in range(numCourses) if indegree[node] == 0)

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next in graph[course]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)

        return order if len(order) == numCourses else []