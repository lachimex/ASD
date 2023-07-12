# bfs
from collections import deque


def bfs(G, s):
    n = len(G)
    distance = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        v = q.popleft()
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                distance[u] = distance[v] + 1
                visited[u] = True
                q.append(u)
    print(distance)
    print(parent)


G = [
    [2, 4],
    [2, 3],
    [0, 1, 4],
    [1, 4],
    [0, 3, 2]
]

bfs(G, 0)