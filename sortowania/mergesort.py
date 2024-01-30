def sort_scal(T, p, r, key):
    if p < r:
        q = (p + r) // 2
        sort_scal(T, p, q, key)
        sort_scal(T, q + 1, r, key)
        merge(T, p, q, r, key)


def sort_scal_r(T, p, r, key):
    if p < r:
        q = (p + r) // 2
        sort_scal_r(T, p, q, key)
        sort_scal_r(T, q + 1, r, key)
        merge_r(T, p, q, r, key)


def merge(T, p, q, r, key):
    solution = []
    pos_a = p
    pos_b = q + 1
    while pos_a <= q and pos_b <= r:
        while pos_b <= r and T[pos_b][key] < T[pos_a][key]:
            solution.append(T[pos_b])
            pos_b += 1
        else:
            solution.append(T[pos_a])
            pos_a += 1
    if pos_a > q and pos_b <= r:
        while pos_b <= r:
            solution.append(T[pos_b])
            pos_b += 1
    elif pos_b > r and pos_a <= q:
        while pos_a <= q:
            solution.append(T[pos_a])
            pos_a += 1
    counter = 0
    for i in range(p, r+1):
        T[i] = solution[counter]
        counter += 1


def merge_r(T, p, q, r, key):
    solution = []
    pos_a = p
    pos_b = q + 1
    while pos_a <= q and pos_b <= r:
        while pos_b <= r and T[pos_b][key] > T[pos_a][key]:
            solution.append(T[pos_b])
            pos_b += 1
        else:
            solution.append(T[pos_a])
            pos_a += 1
    if pos_a > q and pos_b <= r:
        while pos_b <= r:
            solution.append(T[pos_b])
            pos_b += 1
    elif pos_b > r and pos_a <= q:
        while pos_a <= q:
            solution.append(T[pos_a])
            pos_a += 1
    counter = 0
    for i in range(p, r+1):
        T[i] = solution[counter]
        counter += 1


T = [(1, 0), (21, 1), (22, 2), (2, 2), (3, 1), (2, 3)]
sort_scal_r(T, 0, len(T) - 1, 1)
sort_scal(T, 0, len(T) - 1, 0)
print(T)