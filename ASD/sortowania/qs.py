def partition(T, l, r):
    pivot = T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i+1] = T[i+1], T[r]
    return i + 1


def quicksort(T, l, r):
    if l < r:
        q = partition(T, l, r)
        quicksort(T, l, q-1)
        quicksort(T, q+1, r)
    return T


T = [2, 1, 3, 7, 10, 2, 4]
print(quicksort(T, 0, len(T)-1))