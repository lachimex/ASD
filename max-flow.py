from queue import Queue
from math import inf


# def bfs_flow(G, s, t):
#     n = len(G)
#     q = Queue()
#     distance = [inf for _ in range(n)]
#     visited = [False for _ in range(n)]
#     parent = [-1 for _ in range(n)]
#     q.put(s)
#     while not q.empty():
#         v = q.get()
#         if v == t:
#             distance[v] = distance[parent[v]]
#             break
#         visited[v] = True
#         for u in range(n):
#             if G[v][u] > 0 and not visited[u]:
#                 distance[u] = min(distance[u], G[v][u], distance[v])
#                 parent[u] = v
#                 q.put(u)
#     return distance, parent
#
#


def dfs_flow(G, s, t, parent, visited):
    n = len(G)
    visited[s] = True
    if G[s][t] >= 1:
        parent[t] = s
        return True
    for v in range(n):
        if G[s][v] >= 1 and not visited[v]:
            parent[v] = s
            dfs_flow(G, v, t, parent, visited)


def max_flow(G, a, b):
    n = len(G)
    residual_web = G
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    suma = 0

    while True:
        dfs_flow(residual_web, a, b, parent, visited)
        if parent[b] != -1:
            suma += 1
            v = b
            u = parent[b]
            while v != a:
                residual_web[u][v] -= 1
                residual_web[v][u] += 1
                v, u = u, parent[u]
            parent = [-1 for _ in range(n)]
            visited = [False for _ in range(n)]
        else:
            break


    for v in range(n):
        if residual_web[b][v] > 0:
            suma += residual_web[b][v]
    return suma


G = [
    [0, 4, 0, 0, 0, 3],
    [0, 0, 2, 0, 0, 2],
    [0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 0, 2, 0, 2, 0],
]

print(max_flow(G, 0, 3))