def ex19(t, k):
    n = len(t)
    counter = 0
    ruchy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for y in range(n):
        for x in range(n):
            for a, b in ruchy:
                if 0 <= y + a < n and 0 <= x + b < n:
                    if t[y][x] * t[y+a][x+b] == k:
                        counter += 1
    return counter // 2


t = [[2, 6, 4],
     [4, 5, 3],
     [1, 3, 1]]

print(ex19(t,6))