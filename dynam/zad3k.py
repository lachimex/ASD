from zad3ktesty import runtests
from math import inf

def ksuma( T, k ):
    n = len(T)
    F = [inf] * n
    for i in range(k):
        F[i] = T[i]
    for i in range(k, n):
        mini = inf
        for j in range(i - k, i):
            mini = min(mini, F[j])
        F[i] = T[i] + mini
    solution = inf
    for i in range(n-1, n - 1 - k, -1):
        solution = min(solution, F[i])
    return solution
    
runtests ( ksuma )