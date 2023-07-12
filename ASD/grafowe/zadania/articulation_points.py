from math import inf


def art_points(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low = [inf for _ in range(n)]
    d = [inf for _ in range(n)]
    ap = [False] * n
    time = 0

    def dfs_visit(G, u):
        n = len(G)
        nonlocal visited, parent, low, time, ap
        low[u] = time
        d[u] = time
        time += 1
        visited[u] = True

        children = 0
        for v in range(n):
            if G[u][v] >= 1 and not visited[v]:
                children += 1
                parent[v] = u
                dfs_visit(G, v)
                low[v] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= d[u]:
                    ap[u] = True

            elif G[u][v] >= 1 and v != parent[u]:
                low[u] = min(low[u], d[v])

    dfs_visit(G, 0)

    print(ap)


G = [[0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]]

art_points(G)