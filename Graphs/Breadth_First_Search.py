from collections import deque
def bfs(graph,start):
    queue=deque()
    visited=set()
    queue.append(start)
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
graph={
    0:[1,2],
    1:[0,3,4],
    2:[0,5],
    3:[1],
    4:[1],
    5:[2]
}
bfs(graph,0)