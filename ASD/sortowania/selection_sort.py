def selection_sort(tab):
    n = len(tab)
    for i in range(0, n):
        mini = i
        for j in range(i+1, n):
            if tab[j] < tab[mini]:
                mini = j
        tab[i], tab[mini] = tab[mini], tab[i]
    return tab


tab = [2, 1, 3, 7, 10, 1, 5, 2]
print(selection_sort(tab))