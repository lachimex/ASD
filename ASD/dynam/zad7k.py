from zad7ktesty import runtests 


def zbieranie(T, a, b):
    if T[a][b] == 0:
        return 0
    w = len(T[0])
    k = len(T)
    res = T[a][b]
    T[a][b] = 0
    jumps = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    for jump in jumps:
        if 0 <= a + jump[0] < k and 0 <= b + jump[1] < w:
            res += zbieranie(T, a + jump[0], b + jump[1])
    return res


def ogrodnik (T, D, Z, l):
    A = [0] * len(T[0])
    for i in D:
        A[i] = zbieranie(T, 0, i)
    W = [0] * len(D)
    index = 0
    for x in D:
        W[index] = A[x]
        index+=1
    F = [[0] * (l + 1) for _ in range(len(W))]
    for i in range(A[D[0]], l + 1):
        F[0][i] = Z[0]
    for i in range(l + 1):
        for j in range(1, len(W)):
            F[j][i] = F[j-1][i]
            if i - W[j] >= 0:
                F[j][i] = max(F[j][i], F[j-1][i - W[j]] + Z[j])
    return F[len(W) - 1][l]


runtests( ogrodnik, all_tests=True )
