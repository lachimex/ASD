def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)

        i = k = l
        j = mid + 1
        # Copy data to temp arrays L[] and R[]
        while i < mid and j <= r:
            if arr[i] <= arr[j]:
                arr[k] = arr[i]
                i += 1
            else:
                arr[k] = arr[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < mid:
            arr[k] = arr[i]
            i += 1
            k += 1

        while j <= r:
            arr[k] = arr[j]
            j += 1
            k += 1


tab = [2, 1, 3, 7, 8, 3, 1, 4, 5]
mergeSort(tab, 0, len(tab) - 1)
print(tab)
