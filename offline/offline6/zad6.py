# Michał Dydek
# Algorytm polega na utworzeniu grafu gdzie kazda krawedz laczy pracownika z maszyna
# zauwazmy ze bedzie to graf dwudzielny bo nie laczymy ze soba pracownikow ani maszyn
# rozwiazanie zadania sprowadza sie do znalezienia liczby maksymalnych skojarzen w grafie dwudzielnym
# poniewaz zadna maszyna nie moze byc obslugiwana przez wiecej niz jednego pracownika (analogicznie z pracownikami)
# zostal tutaj wykorzystany algorytm forda-fulkersona ktorego zlozonosc czasowa wynosi O ( (V+E) m) gdzie m to wartosc
# maksymalnego przeplywu, aczkolwiek usuwanie krawedzi przy pomocy remove ma zlozonosc O(E),
# wiec ogolna zlozonosc to O ((V+E)E m) zlozonosc pamieciowa O( V+E )

from zad6testy import runtests


def dfs_flow_list(G, s, t, parent, visited):
    for v in G[s]:
        if v == t:
            parent[t] = s
            return True
        else:
            if not visited[v]:
                visited[v] = True
                parent[v] = s
                if dfs_flow_list(G, v, t, parent, visited):
                    return True


def dfs_i_flow_list(G, s, t, parent, visited):
    stos = []
    stos.append(s)
    while stos:
        s = stos.pop()
        for v in G[s]:
            if v == t:
                parent[t] = s
                return True
            if not visited[v]:
                visited[v] = True
                parent[v] = s
                stos.append(v)
    else:
        return False


def max_flow_list(G, a, b):
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    suma = 0
    # if n >= 1000: #stack overflow possibility
    #     while True:
    #         visited[a] = True
    #         dfs_i_flow_list(G, a, b, parent, visited)
    #         if parent[b] != -1:
    #             suma += 1
    #             v = b
    #             u = parent[b]
    #             while v != a:
    #                 G[u].remove(v)
    #                 G[v].append(u)
    #                 v, u = u, parent[u]
    #             parent = [-1 for _ in range(n)]
    #             visited = [False for _ in range(n)]
    #         else:
    #             break
    # else:
    while True:
        visited[a] = True
        if dfs_i_flow_list(G, a, b, parent, visited):
            suma += 1
            v = b
            u = parent[b]
            while v != a:
                G[u].remove(v)
                G[v].append(u)
                # parent[v] = -1
                # visited[v] = False
                v, u = u, parent[u]
            parent = [-1 for _ in range(n)]
            visited = [False for _ in range(n)]
        else:
            break
    return suma


def binworker( M ):
    n = len(M)

    size = n * 2 + 2
    G = [[] for _ in range(size)]

    for pracownik in range(n):
        maszyny = M[pracownik]
        for maszyna in maszyny:
            G[pracownik].append(maszyna + n)

    for i in range(n):
        G[size - 2].append(i)
        G[i+n].append(size - 1)

    return max_flow_list(G, size - 2, size - 1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
