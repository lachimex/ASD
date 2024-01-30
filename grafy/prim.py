from queue import PriorityQueue


def prim(G, s):
    n = len(G)
    parent = [-1 for _ in range(n)]
    inMST = [False for _ in range(n)]
    key = [float("inf") for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s))
    key[s] = 0
    while not q.empty():
        w, v = q.get()
        inMST[v] = True
        for u, w2 in G[v]:
            if not inMST[u] and w2 < key[u]:
                q.put((w2, u))
                key[u] = w2
                parent[u] = v
    return parent


G = [
    [(1, 1), (5, 8), (4, 5)],
    [(0, 1), (2, 3)],
    [(1, 3), (4, 4), (3, 6)],
    [(2, 6), (4, 2)],
    [(0, 5), (3, 2), (2, 4), (5, 7)],
    [(4, 7), (0, 8)]
]

print(prim(G, 0))
