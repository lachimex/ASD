def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def ex15(t):
    n = len(t)
    for y in range(n):
        counter = 0
        for x in range(n):
            a = t[y][x]
            while a != 0:
                if is_prime(a % 10):
                    counter += 1
                    break
                a //= 10
        if counter == n:
            return True
    return False


t = [[2, 3, 6],
     [3, 3, 7],
     [8, 13, 21]]

print(ex15(t))