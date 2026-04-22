class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph={}
        # for i in range(numCourses):
        #     graph[i]=[]
        # for a, b in prerequisites:
        #     graph[b].append(a)
        # def hasCycle(course, visiting):
        #     if course in visiting:
        #         return True
        #     visiting.add(course)
        #     for next in graph[course]:
        #         if hasCycle(next, visiting):
        #             return True
        #     visiting.remove(course)
        #     return False
        # return not any(hasCycle(course, set()) for course in range(numCourses))
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        for a, b in prerequisites:
            graph[b].append(a)
        safe=set()
        visiting=set()
        def hasCycle(course):
            if course in visiting:
                return True
            if course in safe:
                return False
            visiting.add(course)
            for next in graph[course]:
                if hasCycle(next):
                    return True
            visiting.remove(course)
            safe.add(course)
            return False
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True