class DisjointSet:
    def __init__(self, n):
    # Each vertex is its own parent
    self.parent = [i for i in range(n)]

    def find(self, x):
        # Find parent (with path compression)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
    # Join two sets
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
        self.parent[y_root] = x_root

    def kruskal(graph, n):
        # Sort edges by weight
        graph.sort(key=lambda x: x[2])

        ds = DisjointSet(n)
        mst = [] # To store MST edges
        total_cost = 0 # MST total weight

        for u, v, w in graph:
            # Check if adding edge creates cycle
            if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_cost += w

        print("Edges in Minimum Spanning Tree:")
        for u, v, w in mst:
            print(f"{u} -- {v} == {w}")
            print("Total cost of MST:", total_cost)

# Example Graph (u, v, weight)
graph = [
(0, 1, 10),
(0, 2, 6),
(0, 3, 5),
(1, 3, 15),
(2, 3, 4)
]
n = 4 # Number of vertices (0,1,2,3)
kruskal(graph, n)