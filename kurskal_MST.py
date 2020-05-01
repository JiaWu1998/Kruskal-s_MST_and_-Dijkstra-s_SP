# Implementation of Kruskal’s Minimum Spanning Tree Algorithm

# 1. Sort all the edges in non-decreasing order of their weight.
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
# 3. Repeat step 2 until there are (V-1) edges in the spanning tree.

edges = [('R1','R2',200),('R1','R3',500),('R1','R4',10),('R2','R4',70),('R2','R3',80),('R2','R5',90),('R3','R5',40),('R4','R5',200)]
