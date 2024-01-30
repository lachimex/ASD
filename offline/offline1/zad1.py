# Michał Dydek
# algorytm poczatkowo przechodzi przez kazdy element napisu i sprawdza czy moze byc potencjalnie srodkiem nadluzszego palidnromu
# (sprawdzajac czy jest srodkiem palindromu o dlugosci 3) wpisując indeksy potencjalnych srodkow do tablicy indexOfP
# nastepnie iterując po indeksach z tablicy wyliczamy dlugosci palindromow porownując elementy poczatkowo odlegle o 2
# (poniewaz juz sprawdzilismy ze odlegle o 1 są te same), następnie zwiększając i zmniejszając odpowiednie zmienne liczymy dlugosc
# aktualnego palinromu
# Funkcja liczy dlugosc aktualnego palindromu i porownuje to z najdluzszym wczesniej juz znalezionym palindromem
# zlozonosc czasowa w najgorszym przypadku O(n^2)

from zad1testy import runtests


def ceasar(s):
    n = len(s)
    indexOfP = []
    maxi = 1
    for j in range(1, n-1):
        if s[j-1] == s[j+1]:
            indexOfP.append(j)
    for elem in indexOfP:
        a = elem - 2
        b = elem + 2
        while a >= 0 and b < n and s[a] == s[b]:
            a -= 1
            b += 1
        maxi = max(maxi, b - a - 1)
    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ceasar, all_tests = True)
