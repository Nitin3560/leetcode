class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0 

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        answers = []

        for numerator, denominator in queries:
            if numerator not in graph or denominator not in graph:
                answers.append(-1.0)
            else:
                answers.append(
                    dfs(numerator, denominator, set())
                )

        return answers