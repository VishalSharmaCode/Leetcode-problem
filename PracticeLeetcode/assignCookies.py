# Asssign Cookies
g = [4,2,1,6,8]
s = [2,2,3,4,7,1]
def assign(gre, csize):
    gre = sorted(gre)
    csize = sorted(csize)
    count = 0
    l,r = 0, 0
    m,n = len(gre), len(csize)
    while l<m and r< n:
        if gre[l]<= csize[r]:
            count +=1
            l +=1
        r+=1
    return count
        
assign(g,s)