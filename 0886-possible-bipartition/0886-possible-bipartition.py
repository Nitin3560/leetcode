class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        team = {}
        neighbors = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(person, t):
            if person in team:
                return team[person] == t
            team[person] = t
            return all(dfs(disliked, 1 - t) for disliked in neighbors[person])

        return all(dfs(person, 0) for person in range(1, n + 1) if person not in team)