#euler_cycle

def euler_c(G):
    n = len(G)
    solution = []
    start_v = [0] * n

    def dfs_visit(G, v):
        nonlocal solution
        n = len(G)
        for u in range(start_v[v], n):
            if G[v][u] >= 1:
                G[v][u] = 0
                G[u][v] = 0
                start_v[v] = u
                dfs_visit(G, u)
                solution.append(u)

    dfs_visit(G, 0)
    solution.append(0)
    print(solution)


G = [[0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0]]

euler_c(G)