from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, a, b):
        self.graph[a].append(b)

    def DFSutil(self, current, destination, visited):
        if current == destination:
            return True
        visited.add(current)
        for neighbour in self.graph[current]:
            if neighbour not in visited:
                if self.DFSutil(neighbour, destination, visited):
                    return True
        return False

    def is_path(self, start, end):
        visited = set()
        return self.DFSutil(start, end, visited)


g = Graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)

start = int(input("Enter the start node: "))
end = int(input("Enter the end node: "))

if g.is_path(start, end):
    print(f"There is a path from {start} to {end}.")
else:
    print(f"There is no path from {start} to {end}.")