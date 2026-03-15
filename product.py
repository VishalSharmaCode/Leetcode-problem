# Product of Array Except Self
def product(arr):
    arr = [2,3,4,5]
    output = [60,40,30,24]
    temp = []
    for i in range(len(arr)):
        count = 1
        for j in range(len(arr)):
            if j != i:
                count = count * arr[j]
        temp.append(count)
    return temp

def productmain(arr):
    n = len(nums)
    result = [1]*n
    prefix =1
    for i in range(n):
        result[i] =prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i]*= suffix
        suffix *= nums[i]
    return result
    
