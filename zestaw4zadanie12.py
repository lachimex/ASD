def zlozona(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False


def neighbours(t):
    n = len(t)
    solution = 0
    ruchy = [(1,0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for y in range(1, n-1):
        for x in range(1, n-1):
            counter = 0
            for ruch in ruchy:
                a, b = ruch
                if zlozona(t[y+a][x+b]):
                    counter += 1
            if counter >= 6:
                solution += 1
    return solution


def ex12(t):
    n = len(t)
    ilosc = neighbours(t[0])
    for i in range(n-1):
        if ilosc != neighbours(t[i]):
            return False
    return True


t = [[[8, 2, 12], [4, 8, 4], [6, 8, 4]],
     [[8, 2, 12], [4, 8, 4], [6, 8, 4]],
     [[8, 2, 12], [4, 8, 4], [6, 8, 4]]]


print(ex12(t))