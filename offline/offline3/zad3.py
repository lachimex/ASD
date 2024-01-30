# Michał Dydek
# na początku przechodzimy przez wszystkie napisy i jeśli jego odwrotność jest większa to zamieniamy napis na jego odwrotność
# to zapewnia nam, że jeśli w tablicy istnieje napis i jego odwrotność to po przejściu to będą te same napisy
# algorytm polega na stworzeniu max_leng - min_leng kubełków po czym dopasowanie każdego napisu do odpowiedniego kubełka
# opisującego jego długość, po czym posortować je używając radix sorta i na końcu zliczyć powtórzenia tego samego napisu


from zad3testy import runtests


def format_string(s):
    r = s[::-1]
    if r > s:
        return s[::-1]
    else:
        return s


def counting_sort(arr, position):
    n = len(arr)
    output = [""]*n
    count = [0]*26
    for i in range(n):
        count[ord(arr[i][position]) - 97] += 1
    for i in range(1, 26):
        count[i] += count[i - 1]
    for i in range(n-1, -1, -1):
        x = ord(arr[i][position])
        output[count[x - 97] - 1] = arr[i]
        count[x - 97] -= 1
    return output


def radix(T, leng):
    n = leng
    for i in range(n-1, -1, -1):
        T = counting_sort(T, i)
    return T


def strong_string(T):
    n = len(T)
    min_len = float("inf")
    max_len = -1
    for i in range(n):
        T[i] = format_string(T[i])
        x = len(T[i])
        min_len = min(min_len, x)
        max_len = max(max_len, x)
    kubelki = [[] for _ in range(max_len - min_len + 1)]
    for elem in T:
        kubelki[len(elem) - min_len].append(elem)
    maxi = 1
    for elem in kubelki:
        a = len(elem)
        if a > 0 and maxi < a:
            tab = radix(elem, len(elem[0]))
            index = 1
            while index < a:
                naj = 1
                while index < a and tab[index] == tab[index - 1]:
                    naj += 1
                    index += 1
                if naj > maxi:
                    maxi = naj
                index += 1
    return maxi


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
