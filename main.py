from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addedge(self,a,b): #edge = line that connects 2 values in graphs a and b are the points of the line
        self.graph[a].append(b)

    #a function used by DFS - Depth First Search
    def DFSutil(self,v,visited):    
        visited.add(v)
        print(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSutil(neighbour,visited)

    def DFS(self,v):
        #create a set to store visited vertices
        visited = set()
        #call the recursive helper function to print DFS traversal
        self.DFSutil(v,visited)


g = Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)        

print("Following is Depth First Traversal (starting from vertex 0)")
#function call
g.DFS(0)
                
print("Following is Depth First Traversal (starting from vertex 1)")
#function call
g.DFS(1)

print("Following is Depth First Traversal (starting from vertex 2)")
#function call
g.DFS(2)

print("Following is Depth First Traversal (starting from vertex 3)")
#function call
g.DFS(3)

        