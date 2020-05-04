# Implementation of Dijkstras Shortest Path Algorithm

# Step 1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
# Step 2) For all vertices, assign a distance value to all other vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
# Step 3) While sptSet doesn’t include all vertices
#   a) Pick a vertex u which is not there in sptSet and has minimum distance value.
#   b) Include u to sptSet.
#   c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. 
#      For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.

import sys 

class Graph:
    def __init__(self,num_of_vertices):
        self.vertices = num_of_vertices
        # Step 2: Given map[i][k], for every map[i], it is a map of distance values  of all vertices depending on vertex i. 
        self.map = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
    
    def minimum_distance(self, sp_path, compression):
        mini_dst = sys.maxsize
        dest = -1
        for j in range(self.vertices):
            if j not in sp_path and compression[j] < mini_dst:
                mini_dst = compression[j]
                dest = j
        return dest

    def dijkstra_sp(self,source):
        # Step 1: Make solution set
        sp_path = []
        compression = [sys.maxsize] * self.vertices
        compression[source] = 0
        edges = []

        # Step 3
        while len(sp_path) != self.vertices:
            u = self.minimum_distance(sp_path, compression)
            sp_path.append(u)

            #update all adjacent vertices of u
            for adj in range(self.vertices):
                if self.map[u][adj] != 0 and adj not in sp_path:
                    if compression[u] + self.map[u][adj] < compression[adj]: 
                        compression[adj] = compression[u] + self.map[u][adj]
                        
                        exist = False
                        for idx in range(len(edges)):
                            if edges[idx][1] == adj:
                                edges[idx] = (u,adj,compression[adj])
                                exist = True
                        if not exist:
                            edges.append((u,adj,compression[adj]))
        return edges

graph = Graph(5)
graph.map = [
        [0, 200, 500, 10, 0], 
        [200, 0, 80, 70, 90], 
        [500, 80, 0, 0, 40], 
        [10, 70, 0, 0, 200], 
        [0, 90, 40, 200, 0]
        ]; 

orign_edges = []

for x in range(graph.vertices): 
    for y in range(x,graph.vertices):
        if graph.map[x][y] != 0 and (x,y,graph.map[x][y]) not in orign_edges: 
            orign_edges.append((x,y,graph.map[x][y]))

print(f"The original graph has following edges: \n{orign_edges}\n")
print(f"The shortest path tree using dijkstra's SP algorithm has following edges: \n{graph.dijkstra_sp(1)}\n")

