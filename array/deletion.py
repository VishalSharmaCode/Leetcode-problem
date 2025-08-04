def deletion(arr, index):
    n = len(arr)
    item = arr[index]
    for i in range(index, n-1):
        arr[i]= arr[i+1]
    arr.pop()
    return arr

print(deletion([1,2,3,4], 2))