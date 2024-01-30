from zad10ktesty import runtests
from math import sqrt, inf


def dywany ( N ):
    F = [inf] * (N + 1)
    P = [-1] * (N + 1)
    F[0] = 0
    F[1] = 1
    P[1] = 1
    for i in range(2, N + 1):
        counter = 1
        j = 1
        while j <= i:
            if F[i - j] + 1 < F[i]:
                F[i] = F[i - j] + 1
                P[i] = j
            counter += 1
            j = counter * counter
    sol = []
    index = N
    while N > 0:
        sol.append(sqrt(P[index]))
        N -= P[index]
        index -= P[index]


    return sol


runtests( dywany )

