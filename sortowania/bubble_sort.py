def bubble_sort(tab):
    n = len(tab)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab


tab = [2, 1, 3, 7, 10, 1, 12, 5]
print(bubble_sort(tab))
