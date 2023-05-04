def floyd_warshall(G):
    D = G
    n = len(G)
    for t in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][t] + D[t][j])
    return D


G = [
    [0, 3, 8, float("inf"), -4],
    [float("inf"), 0, float("inf"), 1, 7],
    [float("inf"), 4, 0, float("inf"), float("inf")],
    [2, float("inf"), -5, 0, float("inf")],
    [float("inf"), float("inf"), float("inf"), 6, 0]
]

w = floyd_warshall(G)

for row in w:
    print(row)