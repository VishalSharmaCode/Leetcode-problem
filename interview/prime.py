def prime(Num):
    count = 0
    for i in range(2, Num//2+1):
        if Num%i==0:
            count = count+1
    if (count==0):
        return True
    else:
        return False


arr =[]
for i in range(2,10):
    if(prime(i) == True):
        arr.append(i)
print(arr)

arr = []
for i in range(10):
    count = 0
    for j in range(2,i//2+1):
        if i%j ==0:
            count +=1
    if (count == 0):
        arr.append(i)
arr