def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def ex16(t):
    n = len(t)
    for y in range(n):
        for x in range(n):
            counter = 0
            counter2 = 0
            a = t[y][x]
            while a != 0:
                counter2 += 1
                if is_prime(a % 10):
                    counter += 1
                a //= 10
            if counter2 == counter:
                break
        else:
            return False
    else:
        return True


t = [[1, 1, 4],
     [4, 5, 6],
     [7, 8, 9]]

print(ex16(t))