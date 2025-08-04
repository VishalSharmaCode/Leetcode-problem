def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] =arr[j]
            j = j-1
        arr[j+1] =key
    return arr 

arr = [5,3,5,2,3,5,1,6]
print(insertionSort(arr))
    
