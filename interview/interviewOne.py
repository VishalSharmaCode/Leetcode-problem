# Interview Question 
# Add 5 at odd place 
# Multiply 5 at even place
def main(num):
    li = numToList(num)
    li = functionality(li)
    li = singleDigit(li)
    return listToDigit(li)
def numToList(num):
    li = []
    while num != 0:
        li.append(num%10)
        num = num//10
    return li[::-1]

def functionality(li):
    for i in range(len(li)):
        if i%2 ==0:
            li[i] += 5
        else:
            li[i] *= 5
    return li
def singleDigit(li):
    for i in range(len(li)):
        num = li[i]
        li2 = []
        while(num != 0):
            li2.append(num%10)
            num = num//10
        s = sum(li2)
        while (s>9):
            li3 = []
            while(s!=0):
                li3.append(s%10)
                s = s//10
            s = sum(li3)
        li[i] = s
    return li
def listToDigit(li):
    c = 0
    for i in range(len(li)):
        c = c+li[i]
        if i < len(li)-1:
            c = c*10
    return c