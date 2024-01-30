# Michał Dydek
# algorytm polega na znalezieniu k największych wartości, gdzie k jest uzależnione od ilości dni jakie mogą minąć i
# które sprawią, że jakaś chałda śniegu jeszcze będzie. Zauważmy, że kolejność w której bierzemy śnieg z danego obszaru
# nie ma znaczenia, ponieważ k największych wartości zawsze można ułożyć w pewien ciąg, który będzie taki sam jak jego kolejność
# w wyjściowej tablicy. Sumaryczna ilość śniegu jaką weźmiemy będzie wtedy wynosić -> suma k najwiekszych obszarów - ((0 + k - 1)/2 * k).
# Suma ta wynosi maksimum, poniważ bierzemy tyle obszarów, dopóki k + 1 obszar poprzez topnenie śniegu będzie wynosił 0.
# Kierunek wjazdu również nie ma znaczenia, bo taką samą ilość otrzymamy wjeżdzając caly czas od wschodu, od zachodu, jak i na zmianę, lub losowo.
# Złożonośc czasowa algorytmu wynosi O(nlogn), w przypadku kiedy jesteśmy w stanie wziąć cały śnieg. Sprowadza się to do algorytmu sortowania przez kopcowanie.


from zad2testy import runtests


def heapify(S, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and S[left] >= S[i]:
        largest = left
    else:
        largest = i
    if right < n and S[largest] < S[right]:
        largest = right
    if i != largest:
        S[largest], S[i] = S[i], S[largest]
        heapify(S, largest, n)


def build_max_heap(S, n):
    for i in range((n - 2) // 2, -1, -1):
        heapify(S, i, n)


def heap_sort(S, solution, n):
    step = 0
    build_max_heap(S, n)
    for i in range(n - 1, -1, -1):
        if S[0] - step <= 0:  # oznacza to, że nie ma już żadnego śniegu
            break
        solution += S[0] - step
        S[i], S[0] = S[0], S[i]
        step += 1
        heapify(S, 0, i)
    return solution


def snow(S):
    solution = 0
    n = len(S)
    solution = heap_sort(S, solution, n)
    return solution


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
