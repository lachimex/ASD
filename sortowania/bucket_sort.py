def insertion_sort(tab):
    n = len(tab)
    for i in range(1, n):
        j = i
        while j > 0 and tab[j] < tab[j-1]:
            j -= 1
            tab[j], tab[j-1] = tab[j-1], tab[j]


def bucket_sort(T):
    n = len(T)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        buckets[int(n*(T[i]))].append(T[i])
    for i in range(n):
        insertion_sort(buckets[i])
    solution = []
    for i in range(n):
        solution += buckets[i]
    return solution


tab = [2, 3, 1]
insertion_sort(tab)
print(tab)
tab = [0.25, 0.4, 0.5, 0.9, 0.7, 0.24]
print(bucket_sort(tab))