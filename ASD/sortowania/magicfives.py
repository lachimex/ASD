# magic fives

def sort(T, l, r):
    for i in range(l+1, r+1):
        j = i
        while j > l and T[j] < T[j-1]:
            T[j], T[j-1] = T[j-1], T[j]
            j -= 1


def find_median(T, l, r):
    if l == r:
        return T[0]
    mediany = []
    for i in range(l, r+1, 5):
        sort(T, i, min(i + 5, r))
        mediany.append(T[(i + min(i+5, r))//2])
    if len(mediany) == 1:
        return mediany[0]
    else:
        return find_median(mediany, 0, len(mediany) - 1)


def partition(T, l, r, key):
    for i in range(l, r + 1):
        if T[i] == key:
            x = i
            break
    T[x], T[r] = T[r], T[x]
    j = l
    for i in range(l, r):
        if T[i] <= T[r]:
            T[j], T[i] = T[i], T[j]
            j += 1
    T[j], T[r] = T[r], T[j]
    return j


def magic(T, l, r, k):
    if l == r:
        return T[l]
    x = find_median(T, l, r)
    q = partition(T, l, r, x)
    if k == q:
        return T[k]
    elif k < q:
        return magic(T, l, q - 1, k)
    else:
        return magic(T, q + 1, r, k)


tab = [5, 1, 2, 4, 3, 6, 7, 8, 9]
print(magic(tab, 0, len(tab) - 1, 6))