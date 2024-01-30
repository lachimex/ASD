def countSort(arr, position):
    output = [0 for _ in range(len(arr))]
    count = [0 for _ in range(26)]
    for i in arr:
        count[ord(arr[i][position])-97] += 1
    for i in range(1, 26):
        count[i] += count[i - 1]
    for i in arr:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


tab = [1, 7, 5, 2, 3, 1, 6, 2, 5, 4]
print(countSort(tab))