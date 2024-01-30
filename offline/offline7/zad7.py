# Michał Dydek
# Algorytm polega na uprzednim przejsciu pierwszej kolumny i sprawdzeniu czy jest mozliwosc przejscia w dół,
# ponieważ startujemy z pola 0, 0 w tej kolumnie nie interesuje nas przejscie do góry, nastepnie na kazdej kolumnie
# najpierw aktualizujemy wartosc pola do ktorego mozemy dojsc od lewej strony a nastepnie aktualizujemy wartosci najpierw do dolu
# a nastepnie do gory, sprawdzajac czy mozemy wejsc na odpowiednie pole.
# Musimy rowniez patrzyc przy sprawdzaniu dolu i gory na tylko dwa z trzech pol, poniewaz jesli mozemy dojsc do jakiegos pola z gory
# to sciezka z dolu bedzie oznaczala ze sie cofnelismy. Nasza szukana odpowiedzia bedzie max z krancowego pola
# zlozonosc czasowa O(n^2)
# zlozonosc pamieciowa O(n^2)


from zad7testy import runtests


def maze( L ):
    n = len(L)
    T = [[[-1, -1, -1]for _ in range(n)] for _ in range(n)]
    T[0][0] = [0, 0, 0]
    for w1 in range(n):
        if L[w1][0] == '.':
            T[w1][0][0] = w1
        else:
            break
    for j in range(1, n):
        for i in range(n):
            if L[i][j] != '#' and 0 <= j - 1 < n and max(T[i][j-1]) != -1:
                T[i][j][0] = max(T[i][j-1]) + 1
        for i in range(n):
            if L[i][j] != '#' and 0 <= i - 1 < n and max(T[i - 1][j][1], T[i-1][j][0]) != -1:
                T[i][j][1] = max(T[i-1][j][1], T[i-1][j][0]) + 1
        for i in range(n-1, -1, -1):
            if L[i][j] != '#' and 0 <= i + 1 < n and max(T[i + 1][j][2], T[i+1][j][0]) != -1:
                T[i][j][2] = max(T[i + 1][j][0], T[i + 1][j][2]) + 1
    return max(T[n-1][n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
