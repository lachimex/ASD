#bellman ford
from math import inf


def bell_ford(G, s):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance[s] = 0
    for i in range(n-1):
        for v in range(n):
            for u in range(n):
                if G[v][u] != inf:
                    if distance[u] > distance[v] + G[v][u]:
                        parent[u] = v
                        distance[u] = distance[v] + G[v][u]
    for v in range(n):
        for u in range(n):
            if G[v][u] != inf:
                if distance[u] > distance[v] + G[v][u]:
                    return False
    print(distance)
    print(parent)
    return True


G = [[inf, 1, -2, 3, inf, inf, inf],
    [inf, inf, inf, inf, -6, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, 4, inf, inf],
    [inf, inf, 1, inf, inf, 2, 3],
    [inf, inf, inf, -2, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf]]

print(bell_ford(G, 0))