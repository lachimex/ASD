def wycinka(drzewa):
    n = len(drzewa)
    F = [0] * n
    P = [-1] * n
    if n == 1:
        return drzewa[0]
    else:
        F[0] = drzewa[0]
        P[0] = 0
        if drzewa[0] > drzewa[1]:
            F[1] = drzewa[0]
            P[1] = 0
        else:
            F[1] = drzewa[1]
            P[1] = 1
        for i in range(2, n):
            if F[i - 2] + drzewa[i] > F[i - 1]:
                F[i] = F[i-2] + drzewa[i]
                P[i] = i - 2
            else:
                F[i] = F[i - 1]
                P[i] = i - 1
    print(P)
    print(drzewa)
    print(F)
    return max(F)


drzewa = [1, 4, 6, 3, 2, 5, 7, 4, 2, 7, 54, 5]
print(wycinka(drzewa))