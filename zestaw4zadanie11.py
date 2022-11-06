def ex11(t):
    n = len(t)
    t2 = [False] * 10
    counter = 0
    counter2 = 0
    solution = 0
    for i in range(n):
        print("obrot petli numer", i)
        for j in range(n):
            t1 = [False] * 10
            a = t[i][j]
            while a != 0:
                t1[a % 10] = True
                a //= 10
            if i - 1 >= 0:
                counter2 += 1
                b = t[i-1][j]
                while b != 0:
                    t2[b % 10] = True
                    b //= 10
                if t2 == t1:
                    counter += 1
                t2 = [False] * 10
            if i + 1 < n:
                counter2 += 1
                b = t[i+1][j]
                while b != 0:
                    t2[b % 10] = True
                    b //= 10
                if t2 == t1:
                    counter += 1
                t2 = [False] * 10
            if j + 1 < n:
                counter2 += 1
                b = t[i][j+1]
                while b != 0:
                    t2[b % 10] = True
                    b //= 10
                if t2 == t1:
                    counter += 1
                t2 = [False] * 10
            if j - 1 >= 0:
                counter2 += 1
                b = t[i][j-1]
                while b != 0:
                    t2[b % 10] = True
                    b //= 10
                if t2 == t1:
                    counter += 1
                t2 = [False] * 10
            if counter == counter2:
                solution += 1
            counter = 0
            counter2 = 0
    return solution


t = [[132, 123, 2], [321, 321, 213], [3, 231, 4]]
print(ex11(t))