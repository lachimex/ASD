
def dfs(G):
    euler_cycle = []

    def dfs_visit(G, s):
        nonlocal euler_cycle
        n = len(G)

        for u in range(n):
            if G[s][u] > 0:
                G[s][u] = 0
                G[u][s] = 0
                dfs_visit(G, u)
                euler_cycle.append(u)
    dfs_visit(G, 0)
    euler_cycle.append(0)
    return euler_cycle


G = [[0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]]
print(dfs(G))