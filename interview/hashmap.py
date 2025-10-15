# Count Frequency of number and character
def frequencyNumber(items):
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    return frequency
# items = [2,14,18,22,22]
items = "Hello Vishal Sharma Ji"

def freqOfNumber(num):
    convert = str(num)
    frequency = {}
    for item in convert:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item] = 1
    return frequency