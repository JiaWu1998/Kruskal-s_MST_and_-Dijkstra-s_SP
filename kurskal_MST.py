# Implementation of Kruskals Minimum Spanning Tree Algorithm

# Step 1. Sort all the edges in non-decreasing order of their weight.
# Step 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
# Step 3. Repeat step 2 until there are (V-1) edges in the spanning tree.

class Graph: 
    def __init__(self, num_of_vertices): 
        self.V = num_of_vertices 
        self.edges = [] 

    # adds an edge
    def add_edge(self,vertex_1,vertex_2,weight): 
        self.edges.append([vertex_1,vertex_2,weight]) 

    # finds the very first parent/root
    def find(self, parent, i):
        # the very first parent should loop back to itself
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # given two parents, compress the two into one
    def union(self, parent, rank, vertex_1, vertex_2): 
        super_parent_1 = self.find(parent, vertex_1) 
        super_parent_2 = self.find(parent, vertex_2) 
  
        if rank[super_parent_1] < rank[super_parent_2]: 
            parent[super_parent_1] = super_parent_2 
        elif rank[super_parent_1] > rank[super_parent_2]: 
            parent[super_parent_2] = super_parent_1 
        else : 
            parent[super_parent_2] = super_parent_1 
            rank[super_parent_1] += 1

    def kruskals_mst(self): 
        out = []
        i = 0 
        
        # Step 1: sort by weight
        self.edges =  sorted(self.edges,key=lambda e: e[2])
        parent = [] ; rank = []

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        
        # Step 3: repeating step 2 until spanning tree has (V - 1) vertices
        while len(out) < self.V -1:
            vertex_1, vertex_2, weight =  self.edges[i] 
            i = i + 1
            root_of_vertex_1 = self.find(parent, vertex_1) 
            root_of_vertex_2 = self.find(parent ,vertex_2)  

            # Step 2: if root of vertex 1 is not equal to root of vertex 2, then there is no cycle
            if root_of_vertex_1 != root_of_vertex_2: 
                out.append([vertex_1,vertex_2,weight]) 
                self.union(parent, rank, vertex_1, vertex_2)  
        
        return out

graph = Graph(5) 
graph.add_edge(0, 1, 200) 
graph.add_edge(0, 2, 500) 
graph.add_edge(0, 3, 10)
graph.add_edge(1, 3, 70) 
graph.add_edge(1, 2, 80) 
graph.add_edge(1, 4, 90) 
graph.add_edge(2, 4, 40) 
graph.add_edge(3, 4, 200) 


print(f"The original graph has following edges: \n{graph.edges}\n")
print(f"The mininum spanning tree using kurskal's MST algorithm has following edges: \n{graph.kruskals_mst()}\n")