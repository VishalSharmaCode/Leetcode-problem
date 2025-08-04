def selectionSort(arr):
    for k in range(len(arr)-1):
        min = arr[k]
        loc = k
        for i in range(k+1, len(arr)):
            if min > arr[i]:
                min = arr[i]
                loc = i
        temp = arr[k]
        arr[k] = arr[loc]
        arr[loc] = temp
    return arr

print(selectionSort([3,22,5,11,6]))