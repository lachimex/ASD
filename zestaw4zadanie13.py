def is_prime(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 3
    while i * i <= a:
        i += 2
        if a % i == 0:
            return False
        i += 4
        if a % i == 0:
            return False
    else:
        return True

def ex13(t):
    n = len(t)
    t1 = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if t1[y][x] == 0:
                for y2 in range(n):
                    for x2 in range(n):
                        if not x2 == x and y2 == y:
                            if is_prime(t[y][x] + t[y2][x2]):
                                t1[y][x] = t[y][x]
                                t1[y2][x2] = t[y2][x2]
    return t1


t=[[14, 3, 14],
   [1, 1, 1],
   [21, 0, 0]]
print(ex13(t))