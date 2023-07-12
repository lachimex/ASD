from queue import PriorityQueue
from math import inf


def dijsktra_list(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s))
    distance[s] = 0
    while not q.empty():
        d, v = q.get()
        visited[v] = True
        for u, w in G[v]:
            if not visited[u]:
                if distance[u] > d + w:
                    parent[u] = v
                    distance[u] = d + w
                    q.put((d+w, u))
    print(distance)
    print(parent)


def dijsktra_matrix(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance[s] = 0
    for i in range(n):
        mini = inf
        curr_v = -1
        for v in range(n):
            if not visited[v] and distance[v] < mini:
                mini = distance[v]
                curr_v = v
        visited[curr_v] = True
        for u in range(n):
            if not visited[u] and G[curr_v][u] >= 1 and distance[u] > distance[curr_v] + G[curr_v][u]:
                distance[u] = distance[curr_v] + G[curr_v][u]
                parent[u] = curr_v
    print(distance)
    print(parent)