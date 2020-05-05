# Implementation of Dijkstras Shortest Path Algorithm

import sys 

class Graph:
    def __init__(self,num_of_vertices):
        self.vertices = num_of_vertices
        self.adjacency_matrix = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.edges = []
    
    #extracting all edges (only works with undirected graphs)
    def fill_edges(self):
        for x in range(self.vertices): 
            for y in range(x,self.vertices):
                if self.adjacency_matrix[x][y] != 0 and (x,y,self.adjacency_matrix[x][y]) not in self.edges: 
                    self.edges.append((x,y,self.adjacency_matrix[x][y]))

    #find a new vertex that is adjacent to all path vertices and has the shortest distance from source
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
        # Step 2: Given adjacency_matrix[i][k], for every adjacency_matrix[i], it is a map of distance values of all vertices depending on vertex i. 
        compression = [sys.maxsize] * self.vertices
        compression[source] = 0
        edges = []

        # Step 3
        while len(sp_path) != self.vertices:
            # Step 3a: select new adjacent vertex that is not in path and has shortest distance
            u = self.minimum_distance(sp_path, compression)
            # Step 3b: add the new adjacent vertex to path
            sp_path.append(u)

            # Step 3c: update all adjacent vertices of u
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

