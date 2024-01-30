# dfs


def dfs(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d = [-1 for _ in range(n)]
    time = 0

    def dfs_visit(G, v):
        nonlocal time, visited, parent, d
        d[v] = time
        time += 1
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(G, u)

    dfs_visit(G, s)
    print(parent)
    print(d)


G = [
    [2, 4],
    [2, 3],
    [0, 1, 4],
    [1, 4],
    [0, 3, 2]
]

dfs(G, 0)