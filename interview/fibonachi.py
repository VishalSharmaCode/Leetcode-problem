# With range
def fibonacciSeries(Range):
    num1 = 0
    num2 = 1
    num = 0
    arr = []
    while(num < Range):
        arr.append(num)
        num = num1+num2
        num1 = num2
        num2 = num
    return arr

# With Step 
def fibonacciSeries(step):
    num1 = 0
    num2 = 1
    num = 0
    for i in range(step):
        print(num)
        num = num1+num2
        num1 = num2
        num2 = num
        