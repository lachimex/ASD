def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(rank, parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def kruskal(G):
    solution = []
    n = len(G)
    parent = [i for i in range(n)]
    rank = [0]*n
    tab = []
    for v in range(n):
        for u, w in G[v]:
            if v < u:
                tab.append((v, u, w))
    tab = sorted(tab, key=lambda tab: tab[2])
    for u, v, w in tab:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            union(rank, parent, u, v)
            solution.append((u, v, w))
    print(solution)


G = [
    [(1, 1), (5, 8), (4, 5)],
    [(0, 1), (2, 3)],
    [(1, 3), (4, 4), (3, 6)],
    [(2, 6), (4, 2)],
    [(0, 5), (3, 2), (2, 4), (5, 7)],
    [(4, 7), (0, 8)]
]

kruskal(G)