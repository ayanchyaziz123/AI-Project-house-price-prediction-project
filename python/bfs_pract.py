def bfs(graph, start):
    distance =[]
    parent = []
    visited = []

    for i in graph.keys():
        visited[i] = False
        distance[i] = -2
        parent[i] = -1

    print(distance)    






if __name__ == "__main__":
    graph= {
        "Bangladesh":["Pakistan", "India"],
        "India": ["Pakistan", "Bangladesh", "Chin"],
        "Pakistan": ["India", "Bangladesh", "Chin"],
        "Chin": ["India", "Pakistan"]
    }
    bfs(graph, "Bangladesh")