
# Creation 
def creation():
    arr = []
    l = int(input('Give the Length Of Array=>'))
    for i in range(l):
        x = int(input('Give The value=>'))
        arr.append(x)
    return arr

# result = creation()
# print(result)

# Update
def update(arr, ele, pos):
    
    # Add At the last Position
    def addAtLast(arr, ele):
        arr.append(ele)
        return arr
    
    # Replace the Element with postion
    def replace(arr, ele, pos):
        arr[pos] = ele
        return arr
    
    # Replace with element 
    def replaceElement(arr, ele, changewith):
        for i in range(len(arr)):
            if arr[i] == changewith:
                arr[i] = ele
                return arr
        return 'Element now found which you want to update'
    
    # Inser Elemennt at front
    def insert_at_front(arr, ele):
        arr.append(None)
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1] # Shift right
        arr[0] = ele
        return arr
            
        

# Read
def read():
    arr = [1,2,3,4,5,6]
    for i in range(len(arr)):
        print(arr[i])     
# read()



# Delete
class Delete:
    def __init__(self, arr, elements, pos):
        arr = self.arr
        elements = self.elements
        pos = self.pos
        
    def deleteEnd(arr):
        n = len(arr)
        new_arr = [None]*(n-1)
        for i in range(n-1):
            new_arr[i] = arr[i]
        return new_arr
    
    def deleteBeg(arr):
        n = len(arr)
        new_arr = [None]*(n-1)
        for i in range(len(arr)-1):
            new_arr  = arr[i+1]
        return new_arr
    
    def deletePos(arr, pos):
        n = len(arr)
        new_arr = [None]*(n-1)
        
        
