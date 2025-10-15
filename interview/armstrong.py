def armstrongNumber(Num):
    num=Num
    count = 0
    su = 0
    li = []
    while(num != 0):
        li.append(num%10)
        num = num//10
        count+=1
    for i in range(count):
        su = su+li[i]**count
    if su == Num:
        return True
    return False
# Armstrong Number In a range 
for i in range(2000):
    x = armstrngNumber(i)
    if x == True:
        print(i)

     
    
