
def counting_sort(arr, position):
    n = len(arr)
    output = ["" for _ in range(n)]
    count = [0 for _ in range(26)]
    for i in range(n):
        count[ord(arr[i][position]) - 97] += 1
    for i in range(1, 26):
        count[i] += count[i - 1]
    n = len(arr)
    for i in range(n-1, -1, -1):
        output[count[ord(arr[i][position]) - 97] - 1] = arr[i]
        count[ord(arr[i][position]) - 97] -= 1
    return output


def radix(T, leng):
    n = leng
    for i in range(n-1, -1, -1):
        T = counting_sort(T, i)
    return T


tab = ["kot", "kat", "sok", "ala", "bob"]
print(radix(tab, 3))