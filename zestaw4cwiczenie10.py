t = [[0, 2, 3], [1, 0, 2], [2, 0, 1]]
def ex10(t):
    n = len(t)
    wiersze = [False] * n
    kolumny = [False] * n
    for i in range(n):
        for j in range(n):
            if t[i][j] == 0:
                wiersze[i] = True
                break
    for i in range(n):
        for j in range(n):
            if t[j][i] == 0:
                kolumny[i] = True
                break
    for element in wiersze:
        if not element:
            return False
    for element in kolumny:
        if not element:
            return False
    return True

print(ex10(t))