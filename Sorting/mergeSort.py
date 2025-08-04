def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    result = merge(left, right)
    return result
def merge(left, right):
    merged = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex<len(right):
        if left[leftIndex]<right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex +=1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    merged.extend(left[leftIndex:])
    merged.extend(right[rightIndex:])
    return merged

arr = [3,2,8,33,12,90]
print(mergeSort(arr))
