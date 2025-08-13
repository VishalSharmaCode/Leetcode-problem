class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        x = 1
        while(n != 0):
            x = x*n
            n= n-1
        count = 0
        while x != 0:
            if x%10 ==0:
                count +=1
            else:  break
            x = x//10
        return count