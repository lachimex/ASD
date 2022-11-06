import random

def ex18(t):
    n = len(t)
    maks = 0
    coordinates = [0, 0, "null"]
    for y in range(n):
        for x in range(n):
            suma = 0
            counter = 0
            for i in range(x, n):
                counter += 1
                if counter > 10:
                    break
                suma += t[y][i]
            if suma > maks:
                coordinates[0] = y
                coordinates[1] = x
                coordinates[2] = "wiersz"
            maks = max(maks, suma)

    for x in range(n):
        for y in range(n):
            suma = 0
            counter = 0
            for i in range(y, n):
                counter += 1
                if counter > 10:
                    break
                suma += t[i][x]
            if suma > maks:
                coordinates[0] = y
                coordinates[1] = x
                coordinates[2] = "kolumna"
            maks = max(maks, suma)
    return maks, coordinates[0], coordinates[1], coordinates[2]


t = [[-77, -35, 100, -4 , 83 , -88, 89 , 73 , -71, 9  , -11, -6 ,  88],
     [-5 , -40, -36, 91 , -51, 63 , 74 , 36 , 29 , -96, -25, -37, -22],
     [73 , -91, -20, 44 , -16, -1 , 13 , -31, -19, 37 , 89 , 55 , -41],
     [2  , -28, 93 , -14, 88 , -18, -87, -13, -99, 78 , 33 , 23 ,  34],
     [51 , 20 , 39 , -17, 11 , 74 , -75 , 45 , -39, 73, -21, 17 ,  93],
     [73 , 33 , -1 , 74 , 45 , -67, 48 , 90 , -74, -19, -74, -1 , -72],
     [-88, 58 , 14 , -74, -28, 4  , 15 , -37, 63 , 32 , 92 , -78, -12],
     [16 , -63, 22 , -99, -1 , 59 , 84 , 33 , 41 , -2 , 12 , -70, -51],
     [-66, 15 , -33, 64 , 4  , 67 , 38 , -66, 25 , 64 , -85, -42,   4],
     [93 , -81, -53, -6 , -87, 4  , -35, -45, -95, -19, 33 , -40, 100],
     [4  , 17 , -87, -52, -34, 26 , -90, 90 , 42 , 39 , 79 , -52,  -7],
     [76 , -48, -56, -53, 29 , 50 , 35 , -81, -66, 62 , -74, -69,  38],
     [99 , 13 , -91, -89, 74 , -41, -43, -39, -79, -58, -52, 50 , -79]]


print()
print(ex18(t))