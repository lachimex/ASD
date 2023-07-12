#topologic sort

def top(G):
    n = len(G)
    visited = [False for _ in range(n)]
    wynik = []

    def dfs_visit(G, v):
        nonlocal visited, wynik
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(G, u)
        wynik.append(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v)

    wynik = wynik[::-1]
    print(wynik)


G = [
    [1, 2, 3],
    [2, 5],
    [3, 4, 5],
    [],
    [3],
    []
]

top(G)