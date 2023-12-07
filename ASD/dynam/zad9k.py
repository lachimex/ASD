from zad9ktesty import runtests


def prom(P, g, d):
    g = 100
    d = 100
    dp = [[None for i in range(d + 1)] for _ in range(g + 1)]

    def rek(l1, l2, i: int, counter: int, z1, z2):
        if i > len(P) - 1:
            return
        size = P[i]
        if size == 0:
            rek(l1, l2 + size, i + 1, counter + 1, z1, z2 + [i])
            rek(l1 + size, l2, i + 1, counter + 1, z1 + [i], z2)

        if l1 + size > g and l2 + size > d:
            return
        if l1 + size > g:  # gora zajeta
            dp[l1][l2 + size] = (counter + 1, z1, z2 + [i], i, 0)  # liczba zmieszczonych, gorny poklad, dolny poklad, ostatni index, ostatni poklad
            return rek(l1, l2 + size, i + 1, counter + 1, z1, z2 + [i])
        if l2 + size > d:  # dol zajety
            dp[l1 + size][l2] = (counter + 1, z1 + [i], z2, i, 1)
            return rek(l1 + size, l2, i + 1, counter + 1, z1 + [i], z2)

        rek(l1, l2 + size, i + 1, counter + 1, z1, z2 + [i])
        rek(l1 + size, l2, i + 1, counter + 1, z1 + [i], z2)

    M = 0
    indices = []
    rek(0, 0, 0, 0, [], [])
    for i in range(g + 1):
        for j in range(d + 1):
            if dp[i][j] is not None:
                cars_number, up, down, last_index, last_floor = dp[i][j]
                if cars_number >= M:
                    if last_floor == 0:
                        indices = down
                    else:
                        indices = up
                    M = cars_number

    return indices



runtests(prom)

# print(prom([33, 10, 19, 42, 7, 26, 3, 42, 47, 24, 31, 12, 49, 26, 35, 0, 39, 28, 9, 40, 43, 36, 5, 22, 15, 40, 21, 30, 15, 40, 49, 26, 11, 12, 11, 22, 49, 20, 5, 36, 49, 32, 13, 34, 49, 2, 33, 12, 19, 32, 13, 46, 41, 12, 27, 48, 45, 40, 35, 0, 11, 4, 37, 38, 47, 24], 500, 200))
