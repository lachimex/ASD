# dijsktra
from queue import PriorityQueue


def dijsktra(G, s):
    distance = [float("inf") for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    q = PriorityQueue()
    distance[s] = 0
    q.put((0, s))
    while not q.empty():
        d, v = q.get()
        visited[v] = True
        for u, waga in G[v]:
            if not visited[u]:
                if distance[u] > distance[v] + waga:
                    parent[u] = v
                    distance[u] = distance[v] + waga
                    q.put(( distance[u], u))
    print(distance)
    print(parent)


G = [
    [(1, 2), (2, 7)],
    [(0, 2), (2, 3), (4, 4)],
    [(0, 7), (3, 6)],
    [(2, 6), (1, 4)],
    [(1, 4), (3, 1)]
]

dijsktra(G, 0)