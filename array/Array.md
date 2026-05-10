**Array** 
An array is a a DS thata stores homogenious data type of data in a contiguous address.

**Type of Array**
We have mainly three type of array 
1. One Dimensional
2. Two Dimensional  
3. Multi Dimensional 

**CURD On Array**

**Creation**

We Can create Array in Python as Following

1. array = [1,2,3,4]

2. User Input Array
    n = int(input('Provide the Length of array'))
    arr = []
    for i in range(n):
        ele = int(input('Elements =>'))
        arr.append(ele)

3. Using NumPy
    import numpy as np
    arr = np.array([1,2,3,4])

**Read**
We can read array elements using following methods
    1. arr[pos]
    2. for i in range(n):
            print(arr[i])
    3. Search 
        Linear

        def linear(arr, ele):
            for i in range(len(arr)):
                if arr[i] == ele:
                    return i
            return 'Element Not found'
        
        Binary
        
        def binary(arr, ele):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] == ele:
                    return mid
                elif arr[mid] < ele:
                    l = mid+1
                else:
                    r = mid-1
            return 'Element Not Found'

**Update**

**Update Inplace**

def updateInplace(arr, value, position):
    arr[position] = value
    return array

**Insert value In front**

def inserFront(arr, value):
    new_arr = [None]*(len(arr)+1)
    new_arr[0] = value
    for i in range(len(arr)):
        new_arr[i+1] = arr[i]
    return new_arr

**Insert Value At the End** 

Using append

def appendValue(arr, value):
    return arr.append(value)

Manual Approch

def inserEnd(arr, value):
    new_arr = [None]*(len(arr)+1)
    for i in range(len(arr)):
        new_arr[i] = arr[i]
    new_arr[len(new_arr)-1] = value
    return new_arr

**Insert At any possition** 

def inserPossition(arr,value, pos):
    if pos > len(arr):
        return -1
    new_arr = [None]*(len(arr)+1)
    for i in range(pos):
        new_arr[i] = arr[i]
    new_arr[pos] = value
    for i in range(pos+1, len(arr)):
        new_arr[i+1] = arr[i]
    return new_arr

**Delete** 

**Delete From end**

Using remove method
def deleteEnd(arr):
    arr.remove(arr[len(arr)-1])
    return arr

Using Manual approch 
def deleteEnd(arr):
    return arr[0:-1]

**Delete From front**

def deletFront(arr):
    new_arr = [None]*(len(arr)-1)
    for i in range(1,len(arr)):
        new_arr[i-1] = arr[i]
    return new_arr

**Delete by Position**

def deletePosition(arr, pos):
    new_arr = [None]*(len(arr)-1)
    for i in range(pos):
        new_arr[i] = arr[i]
    for i in range(pos,len(arr)-1):
        new_arr[i] = arr[i+1]
    return new_arr

**Delete by Element**

def deletebyElement(arr, ele):
    for i in arr:
        if i == ele:
            arr.remove(ele)
    return arr





        
    
