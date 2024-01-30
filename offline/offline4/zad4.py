# Michał Dydek
# algorytm polega na poczatkowym znalezieniu najkrotszej sciezki prowadzacej z wierzcholka start do wierzcholka end
# nastepnie sprawdza on po kolei każdą z krawędzi czy po jej usunieciu odleglosc miedzy dwoma wierzcholkami sie zwiększy
# ponieważ jeśli istnieje taka jedna krawędź to musi ona znajdowac się na najkrótszej scieżce dlatego, że gdybyśmy
# usuwali krawędzie nienależące do tej ściezki zawsze otrzymalibymsy odleglosc rowna dlugosci najkrotszej sciezki
# sprawdzanie istnienia krawedzi do usuniecia jest realizowane przez krotke del_edge ktora zawiera wspolrzedne dwoch wierzcholkow
# miedzy którymi algorytm nie może przejsc
# zlozonosc czasowa: w pesymistycznym przypadku najkrotsza sciezka bedzie miala dlugosc E
# funkcja bfs_without_parent wywola sie po jednym razie dla kazdej krawedzi z tej sciezki czyli wyjdzie nam O( E(V+E) )
# zlozonosc pamieciowa: O(E) 3 lub 2 tablice w bfsie


from zad4testy import runtests
from collections import deque


def bfs(G, start, end):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    distance = [float("inf") for _ in range(len(G))]
    Q = deque([])
    distance[start] = 0
    visited[start] = True
    Q.append(start)
    while len(Q) != 0:
        v = Q.popleft()
        if v == end:
            break
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                visited[u] = True
                distance[u] = distance[v] + 1
                Q.append(u)
    return distance[end], parent


def bfs_without_parent(G, start, end, del_edge):
    visited = [False for _ in range(len(G))]
    distance = [float("inf") for _ in range(len(G))]
    Q = deque([])
    distance[start] = 0
    visited[start] = True
    Q.append(start)
    while len(Q) != 0:
        v = Q.popleft()
        if v == end:
            break
        for u in G[v]:
            if u < v:
                a = (u, v)
            else:
                a = (v, u)
            if not visited[u] and a != del_edge:
                visited[u] = True
                distance[u] = distance[v] + 1
                Q.append(u)
    return distance[end]


def longer( G, s, t ):
    d, parent = bfs(G, s, t)
    if d == float("inf"):
        return None
    a = t
    while True:
        if a == s:
            break
        if a > parent[a]:
            del_edge = (parent[a], a)
        else:
            del_edge = (a, parent[a])
        d2 = bfs_without_parent(G, s, t, del_edge)
        if d2 > d or (d2 == 0 and s != t):
            return del_edge
        a = parent[a]
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True)
#
