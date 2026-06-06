def sol(nums):
    lArray =[]
    rArray = []
    p = 0
    while p < len(nums):
        lCount = 0
        rCount = 0
        for i in range(p+1, len(nums)):
            rCount += nums[i]
        rArray.append(rCount)
        for i in range(0, p):
            lCount += nums[i]
        lArray.append(lCount)
        p+=1
    res =[]
    print(lArray, rArray)
    for i in range(len(lArray)):
        res.append(rArray[i]-lArray[i])
    res2 = []
    for i in res:
        if i < 0:
            i = i*-1
            res2.append(i)
        else:
            res2.append(i)
    return res2
sol([10,4,8,3])