from queue import Queue

class BFS:
    def __init__(self, graph, source):
        visited = {}
        parent = {}
        dis = {}
        q = Queue()
        output = []

        for x in graph.keys():
            visited[x] = False
            parent[x] = None
            dis[x] = -1

        visited[source] = True
        dis[source] = 0
        
        q.put(source)

        while not q.empty():
            u = q.get()
            output.append(u)

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    dis[v] = dis[u] + 1
                    q.put(v)
        
        print(output)
        print(dis['NEPAL'])

         
if __name__ == "__main__":
    graph = {

        "BANGLADESH" : ["INDIA", "PAKISTAN"],
        "INDIA" : ["BANGLADESH", "PAKISTAN", "CHIN"],
        "PAKISTAN" : ["BANGLADESH", "INDIA", "CHIN"],
        "CHIN" : ["INDIA", "PAKISTAN", "NEPAL"],
        "NEPAL" : ["CHIN"]
    }
    source = "BANGLADESH"
    bbb = BFS(graph, source)
    