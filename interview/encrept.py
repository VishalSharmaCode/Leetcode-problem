st = "AAAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDDDDDDEEEEEEAAAA"
def freq(st):
    freqe = {}
    for item in st:
        if item in freqe:
            freqe[item]+=1
        else:
            freqe[item] = 1
    return freqe
A=freq(st)
print(A)
for i in A:
    print(str(A[i])+i, end = '')
print("")
for i in A:
    print(i+str(A[i]), end = '')