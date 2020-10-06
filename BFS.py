# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
from queue import Queue
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u)
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = {}
        distance = {}
        parent = {}
        queue = Queue()
        bfs_trav_output = []

        for node in self.graph.keys():
            visited[node] = False
            parent[node] = None
            distance[node] = -1
        
        visited[s] = True
        distance[s] = 0
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.put(s)
  
        while not queue.empty(): 
  
            # Dequeue a vertex from  
            # queue and print it 
            x = queue.get()
            bfs_trav_output.append(x)
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for neighbour in self.graph[x]: 
                if visited[neighbour] == False: 
                    visited[neighbour] = True
                    parent[neighbour] = x
                    distance[neighbour] = distance[x] + 1
                    queue.put(neighbour)
        print(bfs_trav_output)  
        print(parent[3])    
        print(distance[3])  
  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 
  


