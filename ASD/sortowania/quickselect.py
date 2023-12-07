def quick_select(T, l, r, k):
    pivot = T[r]
    j = l
    for i in range(l, r):
        if T[i] <= pivot:
            T[i], T[j] = T[j], T[i]
            j += 1
    T[j], T[r] = T[r], T[j]
    if j == k:
        return j
    elif j < k:
        return quick_select(T, j + 1, r, k)
    else:
        return quick_select(T, l, j - 1, k)


# zolnierze

def soldiers(T, p, q):
    n = len(T)
    p = quick_select(T, 0, n - 1, p)
    q = quick_select(T, p, n - 1, q)
    return T[p:q+1]


tab = [170, 172, 167, 340, 220]
print(soldiers(tab, 1, 4))