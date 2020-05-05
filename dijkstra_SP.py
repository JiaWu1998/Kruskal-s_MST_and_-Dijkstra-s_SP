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
        # Step 2: Given adjacency_matrix[i][k], for every adjacency_matrix[i], it is a map of distance values of all vertices depending on vertex i. 
        self.adjacency_matrix = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.edges = []
    
    def fill_edges(self):
        for x in range(self.vertices): 
            for y in range(x,self.vertices):
                if self.adjacency_matrix[x][y] != 0 and (x,y,self.adjacency_matrix[x][y]) not in self.edges: 
                    self.edges.append((x,y,self.adjacency_matrix[x][y]))

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
                if self.adjacency_matrix[u][adj] != 0 and adj not in sp_path:
                    if compression[u] + self.adjacency_matrix[u][adj] < compression[adj]: 
                        compression[adj] = compression[u] + self.adjacency_matrix[u][adj]
                        
                        exist = False
                        for idx in range(len(edges)):
                            if edges[idx][1] == adj:
                                edges[idx] = (u,adj,compression[adj])
                                exist = True
                        if not exist:
                            edges.append((u,adj,compression[adj]))
        return edges

graph = Graph(5)
graph.adjacency_matrix = [
        [0, 200, 500, 10, 0], 
        [200, 0, 80, 70, 90], 
        [500, 80, 0, 0, 40], 
        [10, 70, 0, 0, 200], 
        [0, 90, 40, 200, 0]
        ]; 
graph.fill_edges()

print(f"\nThe original graph has following edges: \n{graph.edges}\n")
source = 1
sp = graph.dijkstra_sp(source)
print(f"The shortest path tree(source = R2 or 1 in our code) using dijkstra's SP algorithm has following edges: \n{sp}\n")
print("Here are the shortest paths from source to all vertices:\n")
print("Source  Destination  Distance\n")
print("-----------------------------\n")

for i in range(len(sp)):
    print(f"R{source+1}           R{sp[i][1]}            {sp[i][2]}\n")

