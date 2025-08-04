def linearSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return 'Element is not in this array'
        
print('Position of element is:>', linearSearch([4,5,6,7,0,1,2], 0))