from collections import deque
def bfs(graph,start):
visited = set()
queue = deque([start])
while queue:
node = queue.popleft()
if node not in visited:
print(node, end=" ")
visited.add(node)
queue.extend(graph.get(node, []))
graph = {
1:[2,3],
2:[4,5],
3:[6,7],
8:[],
9:[],
10:[],
11:[],
}
bfs(graph,1)