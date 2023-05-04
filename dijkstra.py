# dijsktra
from queue import PriorityQueue


def dijsktra(G, s):
    distance = [float("inf") for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    q = PriorityQueue()
    distance[s] = 0
    q.put((s, 0))
    while not q.empty():
        v, d = q.get()
        for u, waga in G[v]:
            if distance[u] > distance[v] + waga:
                parent[u] = v
                distance[u] = distance[v] + waga
                q.put((u, distance[u]))
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