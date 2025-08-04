# we have an array ,item, a position(kth) and the length of array(n)
def insertion(arr, item, kth, n):
    arr1 = [0]*(n+1)
    for i in range(n):
        arr1[i] = arr[i]
    for i in range(kth, n):
        arr1[i+1] = arr[i]
    arr1[kth] = item
    arr[:] = arr1
    return arr

arr = [1,2,4,5]
print(insertion(arr, 3, 2, len(arr)))