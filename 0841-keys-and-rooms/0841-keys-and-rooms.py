class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def explore(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                explore(key)

        explore(0)
        return len(visited) == len(rooms)