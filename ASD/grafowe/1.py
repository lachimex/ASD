# szachownica NxN przejscie krola z lewego gornego do prawego dolnego po polach o najmniejszej sumarycznej sciezce

def dfs(board):
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    mini = float("inf")
    path = []
    current_path = []

    def dfs_visit(board, v, end, sumaric_cost):
        nonlocal mini
        nonlocal path
        if v == end:
            if sumaric_cost < mini:
                mini = sumaric_cost
                path = current_path[:]
                return
        ruchy = ((0, 1), (1, 0), (1, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1))
        for ruch in ruchy:
            v1 = v[0] + ruch[0]
            v2 = v[1] + ruch[1]
            if 0 <= v1 < n and 0 <= v2 < n and not visited[v1][v2]:
                visited[v1][v2] = True
                current_path.append((v1, v2))
                dfs_visit(board, (v1, v2), end, sumaric_cost + board[v1][v2])
                current_path.pop()
                visited[v1][v2] = False
    visited[0][0] = True
    dfs_visit(board, (0, 0), (n - 1, n - 1), board[0][0])
    print(mini, path)


board = [
    [1, 1, 1, 1, 1],
    [2, 5, 2, 2, 2],
    [3, 3, 5, 5, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]

dfs(board)