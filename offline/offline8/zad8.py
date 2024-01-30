#Michał Dydek
# algorytm polega na uprzednim zebraniu wszystkich plam w czasie O(nm), gdzie ilosc paliwa jakiego mozna wydobyc z pola i jest
# rowna plamy[i]. Następnie zachłannie bierzemy największą plamę z zakresu od 0 do aktualna ilosc paliwa, zwiekszamy ilosc zatrzyman
# o 1 i jesli aktualna ilosc paliwa przekroczy parametr k oznacza ze juz moglismy dojechac do ostatniego pola i to nasza odpowiedz
# zlozonosc czasowa O(wk)
# zlozonosc pamieciowa O(k)


from zad8testy import runtests


def zbieranie(T, a, b, w, k):
    wynik = T[a][b]
    T[a][b] = 0
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for move in moves:
        if 0 <= a + move[0] < w and 0 <= b + move[1] < k and T[a + move[0]][b + move[1]] > 0:
            wynik += zbieranie(T, a + move[0], b + move[1], w, k)
    return wynik


def plan(T):
    w = len(T)
    k = len(T[0])
    plamy = [0] * k

    for i in range(k):
        if T[0][i] > 0:
            plamy[i] = zbieranie(T, 0, i, w, k)
        else:
            plamy[i] = 0

    stops = 1
    fuel = plamy[0]
    plamy[0] = 0
    while fuel < k - 1:
        maxi = 0
        max_index = 0
        for i in range(fuel + 1):
            if plamy[i] > maxi:
                maxi = plamy[i]
                max_index = i
        stops += 1
        fuel += maxi
        plamy[max_index] = 0
    return stops


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )