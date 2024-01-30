# Michał Dydek
# algorytm na samym poczatku buduje graf ważony z listy E, gdzie krawedz laczaca dwa wierzcholki ma wage rowna czasu
# potrzebnemu do przebycia miedzy dwiema planetami. Nastepnie uwzględnia osobliwości ktore pozwalaja nam wykonac podroz
# miedzy nimi w czasie zerowym, dodajac do grafu krawedzie o wadze 0. Zauwazmy, że nie musimy łączyc wszystkich
# osobliwosci ze sobą, tylko wystarczy nam polączyć jedną osobliwość, krawędzią o wadze 0 z każdą inną. Jest to poprawne
# poniewaz na przyklad gdy w pierwszym przykladzie chcemy przelecieć z osobliwosci 2 do osobliwosci 3, mozemy wykonac tą trasę
# przelatując przez punkt 0 i dalej zapewni ona nam koszt 0. Nastepnie majac juz tak utworzony graf wykonujemy algorytm Djikstry.
# Złożonośc czasowa:
# e - liczba polaczen miedzy planetami
# n - liczba planet
# O (e + n + e log n) (e na utworzenie grafu z E, maksymalnie n polaczen miedzy osobliwosciami i zlozonosc alg. Djikstry.)
# co sprowadza sie do O (e log n)

from zad5testy import runtests
from queue import PriorityQueue


def spacetravel(n, E, S, a, b):
    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    for i in range(1, len(S)):
        G[S[0]].append((S[i], 0))
        G[S[i]].append((S[0], 0))

    distance = [float("inf") for _ in range(n)]
    q = PriorityQueue()
    q.put((0, a))
    distance[a] = 0
    while not q.empty():
        w, v = q.get()
        for u, waga in G[v]:
            z = waga + w
            if distance[u] > z:
                distance[u] = z
                q.put((z, u))
    if distance[b] == float("inf"):
        return None
    else:
        return distance[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )