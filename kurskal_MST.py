# # Implementation of Kruskals Minimum Spanning Tree Algorithm

# # Part 3
# # 1. Sort all the edges in non-decreasing order of their weight.
# # 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
# # 3. Repeat step 2 until there are (V-1) edges in the spanning tree.

class Graph: 
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def KruskalMST(self): 
        out = []
        i = 0 # An index variable, used for sorted edges 

        self.graph =  sorted(self.graph,key=lambda item: item[2])
        parent = [] ; rank = []
        
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        
        while len(out) < self.V -1:
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v)  
            if x != y: 
                out.append([u,v,w]) 
                self.union(parent, rank, x, y)  
        
        return out

g = Graph(5) 
g.addEdge(0, 1, 200) 
g.addEdge(0, 2, 500) 
g.addEdge(0, 3, 10)
g.addEdge(1, 3, 70) 
g.addEdge(1, 2, 80) 
g.addEdge(1, 4, 90) 
g.addEdge(2, 4, 40) 
g.addEdge(3, 4, 200) 

print(g.KruskalMST())