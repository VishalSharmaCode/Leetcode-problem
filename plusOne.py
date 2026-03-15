# Plus One
def digitcon(arr):
    digit = 0
    i = 0
    j = 10
    while i < len(arr):
        digit = digit+arr[i]
        i = i+1
        digit *= j
    return digit//10
def plusone(arr):
    num = digitcon(arr)
    num = num+1
    arr2 = []
    while num != 0:
        arr2.append(num%10)
        num = num//10
    arr2 = arr2[::-1]
    return arr2
plusone([99])