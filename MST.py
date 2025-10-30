def prim_mst(graph):
n = len(graph) # Number of vertices in the graph
selected = [False] * n # Boolean array to track whether a vertex is
included in MST
key = [999999] * n # Array to store minimum edge weight to
connect each vertex
parent = [-1] * n # To store the parent vertex (used to
reconstruct the MST)

key[0] = 0 # Start from vertex 0 → cost to connect it is 0

# Repeat for (n-1) edges, since MST always has (V-1) edges
for _ in range(n - 1):
# Step 1: Pick the vertex u with the minimum key value that is
not in MST yet
min_key = 999999
u = -1
for v in range(n):
if not selected[v] and key[v] < min_key:
min_key = key[v]
u = v
# Step 2: Include the selected vertex u in the MST
selected[u] = True

# Step 3: Update key values of adjacent vertices of u
for v in range(n):
# If there is an edge from u to v (graph[u][v] != 0)
# AND v is not yet included in MST
# AND weight(u,v) < current key[v], then update
if graph[u][v] != 0 and not selected[v] and graph[u][v] <
key[v]:
key[v] = graph[u][v]
parent[v] = u # Store u as parent of v

# After loop, parent[] contains MST structure
print("Edge Weight")
total_cost = 0
for i in range(1, n):
# parent[i] → i is an MST edge
print(f"{parent[i]} - {i} {graph[i][parent[i]]}")
total_cost += graph[i][parent[i]]
print("Total cost of MST =", total_cost)
# Driver Code
if __name__ == "__main__":
# Graph represented as adjacency matrix (0 = no edge)
graph = [
[0, 2, 0, 6, 0], # Edges from vertex 0
[2, 0, 3, 8, 5], # Edges from vertex 1
[0, 3, 0, 0, 7], # Edges from vertex 2
[6, 8, 0, 0, 9], # Edges from vertex 3
[0, 5, 7, 9, 0] # Edges from vertex 4
]
prim_mst(graph)