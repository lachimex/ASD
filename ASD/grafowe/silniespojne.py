# silnie spojne skladowe


def algorithm(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    stack = []

    def dfs_visit1(graph, v):
        nonlocal stack, visited
        for u in range(n):
            if not visited[u] and graph[v][u] == 1:
                visited[u] = True
                dfs_visit1(graph, u)
        stack.append(v)

    def dfs_visit2(graph, v):
        nonlocal visited
        print(v, end=" ")
        for u in range(n):
            if not visited[u] and graph[v][u] == 1:
                visited[u] = True
                dfs_visit2(graph, u)

    for v in range(n):
        if not visited[v]:
            visited[v] = True
            stack.append(v)
            dfs_visit1(graph, v)

    cords = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                graph[i][j] = 0
                cords.append((j, i))

    for x, y in cords:
        graph[x][y] = 1

    visited = [False for _ in range(n)]

    number = 1
    for v in stack:
        if not visited[v]:
            print("", end="  ")
            print(number, end=" : ")
            number += 1
            visited[v] = True
            dfs_visit2(graph, v)


graph = [
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
]

algorithm(graph)
