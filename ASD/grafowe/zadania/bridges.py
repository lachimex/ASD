# algorithm to find bridges in graph
from math import inf


def find_bridges(G):
    n = len(G)
    parent = [-1 for _ in range(n)]
    low = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    time = 0

    def dfs_visit(G, curr_v, low, parent, visited):
        nonlocal time
        visited[curr_v] = True
        for u in G[curr_v]:
            if not visited[u]:
                low[u] = time
                distance[u] = time
                time += 1
                parent[u] = curr_v
                dfs_visit(G, u, low, parent, visited)
                low[curr_v] = min(low[u], low[curr_v])
            if parent[curr_v] != u:
                low[curr_v] = min(low[u], low[curr_v])

    for v in range(n):
        if not visited[v]:
            low[v] = time
            time += 1
            dfs_visit(G, v, low, parent, visited)

    for v in range(n):
        if distance[v] == low[v] and parent[v] != -1:
            print(v, parent[v])
    print(low)


G = [
    [1, 6],
    [0, 2],
    [6, 3, 1],
    [2, 4, 5],
    [3, 5],
    [3, 4],
    [0, 2, 7],
    [6]
]


find_bridges(G)