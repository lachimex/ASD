def insertion_sort(tab):
    n = len(tab)
    for i in range(1, n):
        j = i
        while j > 0 and tab[j] < tab[j-1]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j -= 1
    return tab


tab = [2, 3, 1, 4, 10, 7, 12, 3]
print(insertion_sort(tab))