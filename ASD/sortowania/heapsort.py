def heapify(T, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and T[left] > T[i]:
        largest = left
    else:
        largest = i
    if right < n and T[largest] < T[right]:
        largest = right
    if largest != i:
        T[largest], T[i] = T[i], T[largest]
        heapify(T, largest, n)


def build_max_heap(T, n):
    for i in range((n-1)//2, -1, -1):
        heapify(T, i, n)



def heap_sort(T):
    n = len(T)
    build_max_heap(T, n)
    for i in range(n):
        T[0], T[n-1] = T[n-1], T[0]
        n -= 1
        heapify(T, 0, n)


T = [3, 7, 8, 2, 4, 34, 12, 78, 6, 9]
heap_sort(T)
print(T)