def creatingArray():
    arr  =[]
    x = int(input('Give the length of array:> '))
    for i in range(x):
        val = int(input('Give the value of array:> '))
        arr.append(val)
    return arr

print('Array:>',creatingArray())

