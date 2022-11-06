def ex17(t):
    n = len(t)
    longest = 0
    coordinates = [0, 0]
    ruchy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for y in range(n):
        for x in range(n):
            maks = 0
            for a, b in ruchy:
                if 0 <= y + a < n and 0 <= x + b < n:
                    maks += t[y+a][x+b]
                if maks > longest:
                    coordinates[0] = y
                    coordinates[1] = x
                    longest = maks
    return coordinates


t = [[2, 3, 1],
     [4, 5, 3],
     [1, 3, 1]]
print(ex17(t))