def ex20(T):
    n = len(T)
    y_wiezy1 = 0
    x_wiezy1 = 0
    y_wiezy2 = 0
    x_wiezy2 = 0
    Y_wiezy1 = 0
    X_wiezy1 = 0
    Y_wiezy2 = 0
    X_wiezy2 = 0
    longest = 0
    for y1 in range(n):
        for x1 in range(n):
            for y2 in range(y1, n):
                for x2 in range(n):
                    T1 = [[False] * n for _ in range(n)]
                    if y1 != y2 or x1 != x2:
                        for y1_T1 in range(n):
                            T1[y1_T1][x1] = True
                        for x1_T1 in range(n):
                            T1[y1][x1_T1] = True
                        for y2_T1 in range(n):
                                T1[y2_T1][x2] = True
                        for x2_T1 in range(n):
                                T1[y2][x2_T1] = True
                        T1[y1][x1], T1[y2][x2] = False, False
                        y_wiezy1 = y1
                        x_wiezy1 = x1
                        y_wiezy2 = y2
                        x_wiezy2 = x2
                        print(T1)
                    suma = 0
                    for y in range(n):
                        for x in range(n):
                            if T1[y][x]:
                                suma += T[y][x]
                    if suma > longest:
                        longest = suma
                        Y_wiezy1 = y_wiezy1
                        X_wiezy1 = x_wiezy1
                        Y_wiezy2 = y_wiezy2
                        X_wiezy2 = x_wiezy2
    return (longest, (Y_wiezy1, X_wiezy1), (Y_wiezy2, X_wiezy2))


T = [[1, 2, 3],
     [4, 5, 6],
     [7, 4, 6]]

print(ex20(T))