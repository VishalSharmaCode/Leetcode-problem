def palandromNumber(number):
    num = number
    num2 = num
    count = 0
    while(num != 0):
        count = count+num%10
        num = num//10
        if (num != 0):
            count = count*10
    if num2 == count:
        return "Palandrom"
    else:
        return "Not A plandrom"