def binarySearch(arr, item):
    first = 0
    last = len(arr)-1
    mid = (first+last)//2
    arr1 = []
    while(first<last and arr[mid] != item):
        if item < arr[mid]:
            last = mid-1
        else:
            first =mid+1
        mid =(first+last)//2
        
    if arr[mid]==item:
        return mid
    else:
        return None
            
print(binarySearch([1,2,3,4,5,6,7,8,9,10,12,14], 12))    