graf = [[0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]


def dfs(graf, root):
    print("odwiedziłem wierzchołek nr ", root)
    n = len(graf)
    for i in range(n):
        if graf[root][i] == 1:
            graf[root][i] = 0
            graf[i][root] = 0
            dfs(graf, i)


dfs(graf, 0)