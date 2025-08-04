class Solution:
    def climbStairs(self, n: int) -> int:
        def fact(num):
            result = 1
            for i in range(2, num+1):
                result *=i
            return result
        
        def nCr(n, r):
            return fact(n)//(fact(r)*(fact(n-r)))

        total_ways = 0
        for k in range(n//2+1):
            one_step = n-2*k
            total_steps = k+one_step
            ways = nCr(total_steps, k)
            total_ways += ways
        return total_ways        