from queue import Queue
from math import inf
def bfs(G, s):
    n = len(G)
    q = Queue()
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    q.put(s)
    while not q.empty():
        v = q.get()
        visited[v] = True
        for u in range(n):
            if G[v][u] > 0 and not visited[u]:
                distance[u] = min(distance[u], G[v][u], distance[v])
                parent[u] = v
                q.put(u)
    return distance, parent